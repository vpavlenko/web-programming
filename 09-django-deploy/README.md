Django: деплой
======================

План лекции
-------

1. Настройка связки nginx <-> uWSGI.
4. Настраиваем PostgreSQL. Переносим данные между базами.
3. Зависимости: requirements.txt.
5. Настройка логгирования. [Sentry](https://getsentry.com/welcome/).
5. Стратегии выкатывания новых версий: гит, тар, деб-пакеты. Deployment keys.
7. Разделение настроек для тестирования/продакшна.
9. Что такое очередь задач.


Что делать после получения ssh-доступа к серверу
---

Я разворачивал DigitalOcean Droplet Ubuntu 14.04 x64. Сайт доступен тут:
[178.62.210.172](http://178.62.210.172/). Репозиторий доступен тут:
[https://bitbucket.org/cxielamiko/testingplatform](https://bitbucket.org/cxielamiko/testingplatform)

```
sudo apt-get update

# Решить проблему с локалью:
# http://la2ha.ru/dev/notes/setting_locale_failed

adduser django
sudo apt-get install python3-dev python3-setuptools
sudo easy_install-3.4 virtualenv

sudo apt-get install nginx
```

Теперь наберите в браузере адрес вашего сервера. Вы должны увидеть домашнюю
страницу nginx.

Обычно, версия nginx, которую можно поставить через aptitude, очень старая,
поэтому рекомендуется поставить свежую с официального сайта самостоятельно.

Когда вы меняете конфиги сервера, перезапускайте его:
```
sudo service nginx restart
```

Cоздайте виртуальное окружение
```
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

Дальше всё по туториалу
http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html
([вот перевод на русский язык](http://habrahabr.ru/post/226419/))

Симлинк `/etc/nginx/sites-enabled/default` можно удалить.

Настройте, чтобы uWSGI стартовал при ребуте.
Сначала проверьте, что uWSGI можно запустить таким образом:
```
/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid django --gid django --daemonize /var/log/uwsgi.log
```

При этом откройте в соседней панели `tmux` лог:
```
tail -f /var/log/uwsgi.log
```

Зайдите в браузере на ваш сайт. Посмотрите, что заход отражается в логах.

После этого добавьте строку запуска uWSGI в `/etc/rc.local/` перед `exit 0`.

Для ребута сервера используйте
```
sudo shutdown -r now
```

При возникновении проблем с `/etc/rc.local` используйте совет по дебагу:
http://serverfault.com/a/391499

Для перезагрузки uWSGI сделайте touch конфигу:
```
touch /etc/uwsgi/vassals/testingplatform_uwsgi.ini
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



Настройка базы PostgreSQL
---

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn

```
sudo apt-get install libpq-dev postgresql postgresql-contrib
su - postgres
createdb testingplatform
createuser -P django
psql
postgres=# GRANT ALL PRIVILEGES ON DATABASE testingplatform TO django;
```

Теперь выполняем из-под пользователя django
```
source /home/django/venv/bin/activate
pip install psycopg2
```

Начало настройки базы MySQL (читайте с конца)
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

1. Задеплойте ваше приложение на VPS-сервер. В [Github Pack](https://education.github.com/pack) есть промокод для DigitalOcean, который позволит бесплатно держать вам сервер за 10$ в течение 10 месяцев. Если у вас нет возможности использовать Github Pack, то можете использовать [Amazon Web Services (AWS)](http://aws.amazon.com/ru/free/). На продукте Elastic Cloud 2 (EC2) всем новым пользователям дают бесплатно один год использования виртуального сервера типа t2.micro.
2. Выделите задачу, которую стоит отложить для очереди задач. Это может быть, например, рассылка писем или индексация для полнотекстового поиска. Реализуйте и задеплойте её.

Залейте изменения в тот же репозиторий и отпишитесь [на странице результатов](https://github.com/vpavlenko/web-programming/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9-%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-7:-Django-1).

Материалы
----

- [Django deployment checklist](https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/)
- [Ротация логов с помощью logrotate](http://linuxnow.ru/view.php?id=50)
- [OpenSSH server security practices](http://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html)
