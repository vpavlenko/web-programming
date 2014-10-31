JavaScript
========



План
----

1. JavaScript: типы данных, conrol flow, доступ к элементам по id и к содержимому, onclick
2. [DOMContentReady](https://gist.github.com/vpavlenko/9092030)
2. jQuery: селекторы, навешивание обработчиков, изменение значений, генерация тегов, перемещение по DOM-дереву
4. Процесс загрузки страницы (вкладка Networks), событие submit формы и его предотвращение
5. Навешивание эвентов к выбранным элементам и к классу



Демонстрации для лекции
---

1. Чистый JavaScript для проверки данных в форме: [click](http://jsfiddle.net/u56uW/6/), [submit](http://jsfiddle.net/u56uW/4/)
4. [Демо по событиям нажатий клавиш](http://javascript.info/tutorial/keyboard-events)
7. [jQuery: селекторы, навешивание обработчиков, изменение значений](http://jsfiddle.net/J45tc/10/)
8. [jQuery: генерация тегов](http://jsfiddle.net/Ta576/2/)
9. [jQuery: перемещение по DOM-дереву](http://jsfiddle.net/5CyNu/3/)
2. Пример выбора поездов: [код](https://github.com/vpavlenko/js-todo-task/tree/master/rasp), [результат](http://vpavlenko.github.io/js-todo-task/rasp/)
3. [Навешивание эвентов к выбранным элементом и к классу](http://jsfiddle.net/8YbM9/1/)


Задания
-------

**1. Todo-list.** Что реализовать в [Todo-list](http://ahamlett.com/Backbone.localStorage/examples/index.html)'е:
- Есть пустой список заданий (список строк), можно добавлять новые строчки. Дело добавляется по нажатию Энтера в поле ввода или по нажатию кнопки "Add".
- Дело можно пометить сделанным. 
- Текст дела можно менять: по двойному щелчку открывается возможность редактирования. (Hint: поищите свойство `contenteditable`.)
- Дело можно удалить из списка. (jquery remove)
- Все дела можно пометить сделанными, а все сделанные дела можно удалить.
- Все дела автоматически сохраняются в LocalStorage. При перезагрузке страницы все дела достаются из LocalStorage.
- Прикручен CSS-фреймворк, и всё выглядит более-менее аккуратно. Или всё очень элегантно свёрстано без фреймворка.


**2. [Календарь](https://github.com/glibin/hh-school-frontend).**


Материалы
--------

1. [Курс по JQuery на Codecademy](http://www.codecademy.com/en/tracks/jquery). Курс по Джаваскрипту на Кодакадеми кажется мне бессмысленным, я его не советую.
2. JavaScript: [Ajax-запросы, асинхронность, замыкания](http://jsfiddle.net/eLeV9/2/), переменное число аргументов, модули, класссы и наследование. 
3. John Resig, Bear Bibeault. Secrets of the JavaScript Ninja. [bookfi.org](http://bookfi.org/) или [twirpx.com](http://www.twirpx.com/).
4. [Building a JavaScript Framework](books/build-a-javascript-framework.pdf)
