Django: деплой
======================

[Скринкаст лекции](http://www.youtube.com/watch?v=EBrxoe1oKEc)

План лекции
-------

1. Настройка связки nginx <-> uWSGI.
4. Настраиваем PostgreSQL. Переносим данные между базами.
3. Virtualenv, requirements.txt.
5. Настройка логгирования. [Logrotate](http://linuxnow.ru/view.php?id=50). [Sentry](https://getsentry.com/welcome/).
5. Стратегии выкатывания новых версий: гит, тар, деб-пакеты. Deployment keys.
7. [Deployment checklist](https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/). Разделение настроек для тестирования/продакшна.


Как задеплоить Джангу
---

**Шаг 1. Получение сервера**

Получите права доступа к VPS-серверу. [Как это сделать через Digitalocean.](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-digitalocean-droplet-virtual-server)

В [Github Pack](https://education.github.com/pack) есть промокод для DigitalOcean, который позволит студентам вузов бесплатно держать сервер за 10$ в течение 10 месяцев. Если у вас нет возможности использовать Github Pack, то можете использовать [Amazon Web Services (AWS)](http://aws.amazon.com/ru/free/). На продукте Elastic Cloud 2 (EC2) всем новым пользователям дают бесплатно один год использования виртуального сервера типа t2.micro.

Я разворачивал DigitalOcean Droplet Ubuntu 14.04 x64. Сайт доступен тут:
[178.62.210.172](http://178.62.210.172/). Репозиторий доступен тут:
[https://bitbucket.org/cxielamiko/testingplatform](https://bitbucket.org/cxielamiko/testingplatform)

**Шаг 2. Чтение туториалов**

Просмотрите [официальный туториал от uWSGI.](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html) [Перевод этого туториала на Хабре.](http://habrahabr.ru/post/226419/)

**Шаг 3. Открытие сессий через tmux**

Залогиньтесь на VPS-сервер под пользователя root. Зайдите под tmux и в дальнейшем все действия выполняйте под ним. Это позволит вам не прекращать ssh-сессии, даже если у вас оборвётся соединение с интернетом. Сессии будут ждать вас до перезапуска сервера.

```
sudo apt-get update
sudo apt-get install tmux
tmux
```

Для входа в существующие сессии при коннекте набираете
```
tmux attach
```

[Шпаргалка по хоткеям tmux](http://habrahabr.ru/post/126996/)

**Шаг 4. Установка nginx**

Обновите репозитории пакетного менеджера и поставьте необходимый софт.

```
sudo apt-get update
sudo apt-get install nginx
```

На Digitalocean может возникнуть проблема с локалью: кодировкой в терминале. Решение описано тут:
http://la2ha.ru/dev/notes/setting_locale_failed


Теперь наберите в браузере адрес вашего сервера. Вы должны увидеть домашнюю
страницу nginx.

Обычно, версия nginx, которую можно поставить через aptitude, старая,
поэтому рекомендуется поставить свежую [с официального сайта](http://wiki.nginx.org/Install) самостоятельно.

Когда вы меняете конфиги сервера, заставляйте nginx перечитать их:
```
sudo service nginx reload
```

При этом конфиги перечитываются. Если в них есть ошибка, ничего не перезапускается, а если ошибок нет, то nginx'у посылается специальный сигнал, который позволяет перечитать конфиги без остановки (и отваливания клиентов).

**Шаг 5. Создание виртуального окружения**

Cоздайте пользователя для старта django-приложения. Создайте из-под него виртуальное окружение.
```
sudo apt-get install python3-dev python3-setuptools
sudo easy_install-3.4 virtualenv

adduser django
login django
cd /home/django
virtualenv venv
```

Теперь как-нибудь перенесите на сервер своё приложение. Например, запакуйте
его через
```
tar cvf testingplatform.tar testingplatform
```
пошарьте через Дропбокс, затем на сервере скажите
```
wget http://dl.dropbox.com/some/path/testingplatform.tar
tar xvf testingplatform.tar
```

Дальше сделайте всё [по туториалу uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html)
([вот перевод на русский язык](http://habrahabr.ru/post/226419/))

Симлинк `/etc/nginx/sites-enabled/default` можно удалить.

**Шаг 6. Настройка автостарта сервера**

nginx автоматически стартует при ребуте. Настройте, чтобы uWSGI также делал это.

Сначала проверьте, что uWSGI можно запустить таким образом:
```
/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --daemonize /var/log/uwsgi.log --uid django --gid django
```

При этом откройте в соседней панели `tmux` лог:
```
tail -f /var/log/uwsgi.log
```

Зайдите в браузере на ваш сайт. Посмотрите, что заход отражается в логах. Прибейте uwsgi: найдите номер мастер-процесс
через `ps` и выполните для него `kill`:
```
root@django-deployment-example:~# ps aux | grep emperor
root       837  0.0  0.1  34268   860 ?        S    11:10   0:00 uwsgi --emperor /etc/uwsgi/vassals --die-on-term --daemonize /var/log/uwsgi.log
root      1398  0.0  0.1  11760   940 pts/0    S+   11:16   0:00 grep --color=auto emperor
root@django-deployment-example:~# kill -9 837
root@django-deployment-example:~# ps aux | grep emperor
root      1430  0.0  0.1  11756   944 pts/0    S+   11:17   0:00 grep --color=auto emperor
root@django-deployment-example:~#
```

Внимание: **нельзя** выносить параметры uid/gid в `.ini`-конфиг вассала. Чем это опасно? Пусть в коде вашего приложения закралась уязвимость, которая позволит злоумышленнику выполнять произвольные действия от пользователя django. В частности, мой пример testingplatform подвержен такой уязвимости, поскольку получает от клиента и выполняет произвольный питоновский код с правами django. Поскольку `.ini`-файл доступен на редактирование пользователю django, это позволит злоумышленнику указать в конфиге uid=root и после очередного рестарта сервера повысить свои привелегии до рута. Для uwsgi опция uid, переданная из командной строки, имеет приоритет перед такой же опцией, указанной в конфигурационном файле, поэтому передача их в командной строке позволяет обезопасить себя от атаки с этой стороны.

Туториал по uWSGI предлагает добавить строку запуска uWSGI в `/etc/rc.local` перед `exit 0`.
[В этой статье](http://bencane.com/2011/12/30/when-its-ok-and-not-ok-to-use-rc-local/)
объясняется, почему так не стоит делать.

Вместо этого давайте использовать механизм Upstart старта сервисов в Убунте.
Создайте скрипт `/etc/init/uwsgi.conf` с содержимым
```
# simple uWSGI script

description "uwsgi tiny instance"
start on runlevel [2345]
stop on runlevel [06]

exec uwsgi --emperor /etc/uwsgi/vassals --die-on-term --logto /var/log/uwsgi.log
```

Для управления uwsgi через Upstart теперь можно использовать
```
start uwsgi
stop uwsgi
status uwsgi
restart uwsgi
```

Для ребута сервера используйте
```
sudo shutdown -r now
```

Если вы сделали изменения в Django-коде, то рестартовать uWSGI можно и так:
```
touch /etc/uwsgi/vassals/testingplatform_uwsgi.ini
```

TODO: подумать, хорошо ли, что uwsgi emperor запущен от рута.


Настройка базы PostgreSQL
---

Всё можно сделать по этой статье: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn

Вводим в терминале из-под рута:

```
apt-get install libpq-dev postgresql postgresql-contrib
su - postgres
createdb testingplatform
createuser -P django
psql
postgres=# GRANT ALL PRIVILEGES ON DATABASE testingplatform TO django;
```

Теперь выполняем из-под пользователя django:
```
source /home/django/venv/bin/activate
pip install psycopg2
```



Перенос данных из одной базы в другую
---

**Шаг 1.** Выполняется со старыми настройками DATABASES в settings.py
```
python manage.py dumpdata > datadump.json
```

**Шаг 2.** Выполняется с новыми настройками DATABASES в settings.py
```
python manage.py loaddata datadump.json
```




Неоконченная попытка настроить MySQL
---

```
# Установка базы
sudo apt-get install mysql-server-5.6 libmysqlclient-dev
source venv/bin/activate
pip install mysqlclient
# Проблема установки появляется из-за нехватки оперативной памяти.
# Решение: добавить больше памяти или создать своп-раздел.
# http://askubuntu.com/questions/457923/why-did-installation-of-mysql-5-6-on-ubuntu-14-04-fail

# Далее создаём базу для приложения и настраиваем пользователя и права:
mysql -p
mysql> CREATE DATABASE testingplatform;
mysql> CREATE USER 'django'@'localhost' IDENTIFIED BY 'Aelaef0l';
mysql> GRANT ALL PRIVILEGES ON testingplatform.* TO 'django'@'localhost';
mysql> FLUSH PRIVILEGES;

# Дописываем настройки в settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testingplatform',
        'USER': 'django',
        'PASSWORD': 'Aelaef0l',
    }
}

# Создаём все таблицы в новой базе
python manage.py migrate

# На этапе переноса данных я поймал проблемы с Юникодом в MySQL.
# Подробности:
# http://stackoverflow.com/a/20349552
# https://mathiasbynens.be/notes/mysql-utf8mb4
```


Задание
------

Продолжайте развивать проект, который вы начали делать в прошлый раз.

Задеплойте ваше приложение на VPS-сервер. Отпишитесь [на странице результатов](https://github.com/vpavlenko/web-programming/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9-%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-7:-Django-1).

Материалы
--

- [Г. Курячий, К. Маслинский. Операционная система Linux](http://docs.altlinux.org/books/altlibrary-linuxintro2.pdf)

