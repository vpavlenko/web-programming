Cookies, sessions, пользователи
======================


План лекции
-------

1. Простой деплоймент: Vagrant, [tmux](https://gist.github.com/henrik/1967800), [gunicorn](http://flask.pocoo.org/docs/0.10/deploying/wsgi-standalone/#gunicorn). VPS, DigitalOcean. [Github Pack](https://education.github.com/pack).
2. [Тестирование Flask-приложений.](http://flask.pocoo.org/docs/0.10/testing/)
3. Декораторы: `functools.lru_cache`, `logging`, `counter`.
4. Форма логина ползователя без пароля. Cookies.
5. Логин с паролем: как передается пароль по сети. HTTPS.
6. Как хранить пароль: хэши, солёные хэши.
6. Sessions.

Задание
------

1. Расширить функционал сокращателя ссылок: добавить логин пользователей (лучше - с паролем). Пользователь может просматривать все созданные им сокращенные ссылки.

2. Написать тесты на функционал сокращателя ссылок.

2. Расширить функционал блога:
    - Добавить форму регистрации
    - Сделать правильные перенаправления
    - Добавить возможность подписываться на чужие блоги и читать ленту друзей.
    - Добавить возможность делать записи "только для себя" и "только для друзей"

Материалы
---

1. [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
