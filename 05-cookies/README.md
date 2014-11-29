Деплой и тестирование, Cookies, форма логина
======================

Скринкасты
-------

1. [Vagrant, tmux, gunicorn](http://www.youtube.com/watch?v=3zRuMyt7yyc)
2. [Тестирование Flask-приложений](http://www.youtube.com/watch?v=KaGouI9ZaIo)
3. [Travis CI](http://www.youtube.com/watch?v=oSBXaJLBErg)
4. [Форма логина пользователя без пароля. Cookies](http://www.youtube.com/watch?v=hn_zebvViVI)

План недели
-------

1. Простой деплоймент: Vagrant, [tmux](https://gist.github.com/henrik/1967800), [gunicorn](http://flask.pocoo.org/docs/0.10/deploying/wsgi-standalone/#gunicorn). VPS, DigitalOcean. [Github Pack](https://education.github.com/pack).
2. [Тестирование Flask-приложений.](http://flask.pocoo.org/docs/0.10/testing/)
3. Virtualenv, Travis CI.
4. Форма логина пользователя без пароля. Cookies.
5. Логин с паролем: как передается пароль по сети. HTTPS.
6. Как хранить пароль: хэши, солёные хэши.
6. Sessions.

Задание
------

1. Расширьте функционал сокращателя ссылок: добавить логин пользователей (лучше - с паролем). Пользователь может просматривать все созданные им сокращенные ссылки.

2. Напишите тесты на функционал сокращателя ссылок.

3. В репозитории "сокращатель ссылок" настройте запуск тестов через Travis CI. В корень репозитория добавьте файл README.md, вставьте в него build badge Трэвиса.

4. Задеплойте сокращатель ссылок на VPS-сервер. Если у вас нет возможности использовать Github Pack, то можете использовать Amazon Web Services (AWS). На продукте Elastic Cloud 2 (EC2) всем новым пользователям [дают бесплатно один год использования](http://aws.amazon.com/ru/free/faqs/) виртуального сервера типа t2.micro.

5. В заголовке своего репозитория добавьте ссылку на задеплоенный сервис.

Ссылки на свой репозиторий добавьте [на вики-страничку](https://github.com/vpavlenko/web-programming/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9-%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-5).



Материалы
---

1. [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
2. [HTTP Cookie - русская Википедия](https://ru.wikipedia.org/wiki/HTTP_cookie)
3. [VPS - русская Википедия](https://ru.wikipedia.org/wiki/VPS)
4. [Статья про солёные хэши](http://www.internet-technologies.ru/articles/article_1807.html)
