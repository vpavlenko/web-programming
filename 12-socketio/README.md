Node.js, Socket.io и облачный хостинг
===

План лекции
---

- Node.js: однопоточность, event loop
- [Socket.io](http://socket.io/get-started/chat/): [chat demo](http://socket.io/demos/chat/)
- [Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs): [hello world](https://dry-bastion-7907.herokuapp.com/), [chat](https://pacific-crag-7875.herokuapp.com/)
- Обсуждение: как реализовать синхронизацию многопользовательского списка дел или графического редактора при обрывах сети
- [MoscowSocial](http://bit.ly/MoscowSocial)


Задание
-------

1. Создайте для вашего списка дел бекенд на Express.js. Все данные пока храните в памяти запущенного сервера.

2. Реализуйте возможность добавления новых дел и автоподгрузки новых дел, добавленных другими. Используйте для этого Socket.io.

3. Задеплойте ваше приложение на Heroku.


Материалы
--

**Node.js**
- [Understanding the node.js event loop](http://blog.mixu.net/2011/02/01/understanding-the-node-js-event-loop/)
- Хэррон Д. Node.js. Разработка серверных веб-приложений на JavaScript

**Socket.io**
- [Pushing with Flask, Armin Ronacher's post](http://lucumr.pocoo.org/2012/8/5/stateless-and-proud/)
- [EventSource - события с сервера](http://learn.javascript.ru/server-sent-events)
- [Описание протокола WebSocket](http://learn.javascript.ru/websockets)

**Облачный хостинг**
- [Twelve-Factor App: манифест кофаундера Heroku](http://12factor.net/)
- [Критическая статья про Heroku](http://tech.blog.aknin.name/2012/03/09/heroku-is-great-however/)
