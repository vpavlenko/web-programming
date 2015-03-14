Графические компоненты (виджеты)
======================

Скринкасты лекции
--

- [Графические компоненты, шаблонизаторы](http://www.youtube.com/watch?v=iv2Vl_rzQjw)
- [Практическая работы](http://www.youtube.com/watch?v=i0Meqqp7fMo)

План лекции
-------

1. Обсуждение [серии статей про виджеты](http://learn.javascript.ru/widgets).
2. [Range slider](range-slider), [демо](http://vpavlenko.github.io/web-programming/10-widgets/range-slider/). [Вдохновение](http://refreshless.com/nouislider/).
2. Обсуждение шаблонизатора [swig](http://paularmstrong.github.io/swig/)



Практическое задание
--

**Задача:** сверстать меню кафе и сделать динамическую фильтрацию списка блюд по диапазону цены. Для этого взять данные, скрестить их с шаблонизатором, дописать код слайдеру и собрать демо.

1. Возьмите список блюд и цены [отсюда](http://www.zucafe.ru/index.php?id=26). Придумайте способ преобразовать его в json без повторяющихся действий руками. Если нужно, используйте электронные таблицы, экспорт в CSV, множественные курсоры в текстовых редакторах.
2. Сверстайте одну строку меню.
3. С помощью шаблонизатора [swig](http://paularmstrong.github.io/swig/) превратите вёрстку в шаблон. Отрисуйте на странице json-данные через шаблон.
3. Возьмите заготовку [range slider](range-slider) за основу. Измените код так, чтобы функция value() возвращала текущее значение интервала.
4. Добавьте на страницу кнопку "Фильтровать". При нажатии на эту кнопку считывается значение слайдера, по нему фильтруется массив данных, отфильтрованный json-список рендерится в поле меню.
2. Реализуйте способ пользователю передавать формат надписи над лапками слайдера. Например: число с двумя знаками после запятой, число со знаком %/$.
6. Добавьте пользователю возможность передать колбек, который вызывается при изменении значения слайдера. В колбеке сделайте то же, что происходит при нажатии кнопки "Фильтровать".

Выложите решение на JsFiddle, CodePen или Github Pages. Ссылку добавьте [на вики-страницу для решений](https://github.com/vpavlenko/web-programming/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-10:-%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82).

Мой результат: [код](range-slider), [демо](http://vpavlenko.github.io/web-programming/10-widgets/range-slider/demo.html).


Библиотеки компонентов
---

- [Виджеты в стандарте HTML5](http://diveintohtml5.info/forms.html)
- [Bootstrap components](http://getbootstrap.com/components/)
- [Foundation components](http://foundation.zurb.com/docs/)
- [JQuery UI](http://jqueryui.com/)


Курсы по теме на HTMLAcademy
---

- [Мастерская: создаём меню](https://htmlacademy.ru/courses/50)
- [Мастерская: декоративные элементы](https://htmlacademy.ru/courses/55)
- [Формы и HTML5](https://htmlacademy.ru/courses/74)



Домашнее задание
------

Выберите один виджет и реализуйте его так, как считаете нужным. Выложите его на CodePen. Ссылку добавьте [на вики-страницу для решений](https://github.com/vpavlenko/web-programming/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-10:-%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82).


Примеры виджетов
---

**Навигация**

5. Menu/dropdown
1. Tabs
1. Accordion
6. Button group / pagination
16. Image slider
13. Tree (folders)

**Компоненты форм**

1. Selectbox
12. Multiple selection
6. Autocomplete
17. Range slider
10. Slider
1. Star rating
10. Datepicker
11. Colorpicker

**Датчики и уведомления**

7. Alert
8. Popup
9. Progress bar
10. Tooltip
14. Badges



Материалы
---

- Emmet - плагин для быстрого набора HTML и CSS: [demo](http://emmet.io/), [cheat sheet](http://docs.emmet.io/cheat-sheet/)
- [Создание графических компонентов (виджетов)](http://learn.javascript.ru/widgets)
- [10 правил хороших форм](http://www.artlebedev.ru/tools/technogrette/etc/forms/)
