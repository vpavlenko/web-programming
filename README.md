Веб-программирование на Физтехе
===============

[![Build Status](https://travis-ci.org/vpavlenko/web-programming.svg?branch=master)](https://travis-ci.org/vpavlenko/web-programming)

Спецкурс читался в МФТИ в Долгопрудном в 2014-2015 учебном году.

[Видеолекции курса есть на Ютьюбе](http://www.youtube.com/playlist?list=PLzQrZe3EemP5KsgWGnmC0QrOzQqjg3Kd5)

**Ещё у меня есть начальный курс Питона [Snakify.org](https://snakify.org/) с интересными задачами**

Курсы на Физтехе в 2015-2016 году
--
- **Веб-программирование, лектор Вадим Марковцев.** [Материалы](http://vmarkovtsev.github.io/mipt_web_2015/00_overview/index.html), [группа в ВК](https://vk.com/mipt_web).
- **Компьютерная безопасность и CTF.** [Репозиторий](https://github.com/xairy/mipt-ctf), [группа в ВК](https://vk.com/mipt_ctf).
- **Анализ данных.** [Репозиторий](https://github.com/vkantor/MIPT_Data_mining_in_action_2015), [группа в ВК](https://vk.com/data_mining_in_action).

Осенний семестр
----

**29 октября.** [Какие языки и технологии используются на вебе. HTML. CSS. CSS-фреймворки. Хостинг для статического сайта.](01-html-css)

**5 ноября.** [Javascript. Управляющие конструкции, типы данных, примеры работы с деревом элементов. Библиотека JQuery. Github.io.](02-js)

**12 ноября.** [Введение в язык Python 3.](03-python)

**19 ноября.** [Протокол HTTP. Реализация своими руками: веб-фреймворк на голых сокетах. "Сокращатель ссылок". Фреймворк Flask: routing, шаблоны. "Блог". Тестирование Flask-приложения.](04-http)

**26 ноября и 3 декабря.** [Менеджер виртуальных машин Vagrant. Деплоймент на VPS через tmux и gunicorn. Тестирование Flask-приложений, Travis CI. Cookies, sessions. Передача и хранение паролей, HTTPS. Декораторы](05-cookies)

Весенний семестр
---

**20 февраля.** [Язык SQL. Sqlite3, работа с базой sqlite3 из Питона. Фреймворк Django: ORM, админский интерфейс базы](07-django-1)

**27 февраля.** [Django: статика, регистрация пользователей, ajax, JSON API, кастомизация админки, миграции базы, XSS](08-django-2)

**6 марта.** [Деплоймент: nginx, uWSGI, PostgreSQL, логгирование](09-django-deploy)

**13 марта.** [Графические компоненты (виджеты)](10-widgets)

**20 марта.** [Node.js: зачем нужна асинхронность. Npm. Автоматизация фронтенда: Bower, Grunt, JSHint, LESS, ES6](11-bower-grunt)

**27 марта.** [Node.js, Express.js. Socket.io. Облачный хостинг: heroku](12-socketio)

**1 апреля.** [Гостевая лекция: Дмитрий Елисов о том, что бизнес надо делать на простых технологиях](http://www.slideshare.net/cxielamiko/web-programmin-guest-lecture-dmitry-elisov)

**8 апреля.** [Фреймворки для одностраничных приложений: концепция MVC, виртуальное DOM-дерево](14-spa)

**15 апреля.** [Тестирование фронтенда: QUnit, Mocha, Karma. Тестирование API: requests. Selenium WebDriver](15-selenium)

**22 апреля.** [React.js](17-react). Кроме того, [Плагины для Хрома. Букмарклеты](16-bookmarklets)

**29 апреля.** [WordPress, создание интернет-магазина на WooCommerce](18-final)


Проект нашего ученика
--

[**Миптакар**](http://miptacar.ru/) - сайт поиска попутчиков на Физтехе


Что не рассказано на курсе
-----

**Вёрстка**
- Сетки, позиционирование. Декоративные элементы. Вёрстка меню
- Вёрстка писем
- Вёрстка для мобильных устройств
- Вёрстка для печати

**Фронтенд**
- Yeoman
- Normalize.css
- Препроцессоры HTML: Jade, HAML
- Современные CSS-препроцессоры Sass, Stylus
- Языки, компилируемые в JavaScript: CoffeeScript, Dart, Closure Compiler
- Зависимости в JavaScript: AMD, Require.js, CommonJS, ES6-подход
- Векторная графика на вебе: raphael, d3.js
- Web Components, Polymer
- Как лечить [scrolling amnesia](https://cldup.com/3m0DOKp9BW.gif)?

**Бекенд**
- Полнотекстовый поиск
- Авторизация через соцсети
- Кеширование
- Безопасность. Атаки, механизмы защиты
- Очередь задач: celery

**Разное**
- Проектирование интерфейсов
- Читаем чужой код: [сервис Plunker](https://github.com/filearts/plunker)
- Интернационализация
- Яндекс.Метрика. [Микроформаты](http://habrahabr.ru/hub/microformats/)

Материалы
--

**Фронтенд**

- [Scalable and Modular Architecture for CSS](https://smacss.com/)
- [Какие фреймворки используются на популярных сайтах](https://docs.google.com/spreadsheets/d/1OChsdXnXY8mTums6BhzrIvjTiDbJLry5QTSJkxf8OmY/edit#gid=0)
- [7 Principles of Rich Web Applications](http://rauchg.com/2014/7-principles-of-rich-web-applications/#push-code-updates)
- [HTML5 Game Development - Udacity Online Course](https://www.udacity.com/course/cs255)

**Бекенд**
- [А. Ю. Васильев. Работа с PostgreSQL: настройка и масштабирование](http://postgresql.leopard.in.ua/html/)
- [Spot vs. EC2 instances on Amazon](http://stackoverflow.com/questions/5188871/aws-amazon-ec2-spot-pricing/11996798#11996798)
- [Лекции Техносферы. 1 семестр. Методы использования СУБД в интернет-приложениях](http://habrahabr.ru/company/mailru/blog/256039/)
