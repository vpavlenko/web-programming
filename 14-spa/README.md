Single page applications, виртуальное DOM-дерево
===

Лекция велась на меловой доске, скринкаста и записи не велось.


Как проектировать Todo-list
---

[Мокап](https://moqups.com/cxielamiko@gmail.com/d4u4exgg/)

![](images/overview.png)

- В каких случаях надо отрисовывать новое дело?

- Можем ли хранить данные в ДОМ-дереве?

- Сколько шаблонов на этой странице потребуется?

- Как хранимые данные синхронизируются с сервером?

![](images/model-detail.png)

- Когда надо перерисовывать шаблоны?

- Нужно ли перерисовывать все шаблоны на странице? Это может быть плохо?

- Пусть пользователь - это отдельная сущность в бекенде, у него есть id, имя, аватарка, статус "онлайн". Что поменяется в хранении моделей?

- Что будет происходить, когда связь с сервером оборвётся, а потом восстановится?

- Роутинг.


Материалы
---

**Конкретная философия**
- [Single page apps in depth](http://singlepageappbook.com/index.html)
- [Riot.js](https://muut.com/blog/technology/riotjs-the-1kb-mvp-framework.html), [Riot 2.0](https://muut.com/blog/technology/riot-2.0/index.html)

**Фреймворки**
- TodoMVC: [Backbone.js](http://todomvc.com/examples/backbone/), [Angular.js](http://todomvc.com/examples/angularjs/#/)
- [Backbone.js для «чайников»](http://habrahabr.ru/post/127049/)
- [Написание сложных интерфейсов с Backbone.js](http://m.habrahabr.ru/post/118782/)
- [AngularJS’ Internals In Depth](http://www.smashingmagazine.com/2015/01/22/angularjs-internals-in-depth/)
- [Getting Started with Mithril](http://lhorie.github.io/mithril/getting-started.html)

**Абстрактная илософия**
- [Илья Бирман. Будущее нативных и веб-приложений](http://ilyabirman.ru/meanwhile/all/web-or-native-future/)
- [Не учите фреймворки, учите архитектуру](http://habrahabr.ru/post/253297/)
- [MVC умер, пришло время MOVE (читайте комментарии)](http://habrahabr.ru/post/147038/)
