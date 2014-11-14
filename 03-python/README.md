Python
======================

[Скринкаст первой части лекции](http://www.youtube.com/watch?v=O2k1kL1NUvs)

[Скринкаст второй части лекции](http://www.youtube.com/watch?v=zZ13ZBgTjIQ)

Что нужно установить
--------

Установите Python3. Для заданий 7-9 также понадобятся setuptools и pip. При желании установите текстовый редактор [Sublime Text](http://www.sublimetext.com/) или среду разработки [PyCharm](http://www.jetbrains.com/pycharm/).

**Установка для Виндоус**

Устанавливаем [Python3](http://python.org/download/), [setuptools](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools)
и [pip](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip).

**Установка для Убунты**

    sudo apt-get install python3
    sudo apt-get install python3-setuptools
    sudo easy_install3 pip

**Установка для Мака**

	sudo port install python33
	# будет доступен в /opt/local/bin/python3.3
    
	sudo port install py33-pip
	# будет доступен в /opt/local/bin/pip-3.3


План лекции
-------

1. [Арифметика, списки, строки, множества, словари, if, for](python_examples.py)
2. [Словари, срезы](python_examples_2.py)
3. [min/max, функции, lambda](python_examples_3.py)
3. [Файловый ввод-вывод](http://pythontutor.ru/lessons/file_io/)
6. [Объектно-ориентированное программирование](oop)
7. [Функция cmp_to_key](comparator.py)


Как сдавать решения
-------------------

1. Залейте решение на [gist.github.com](https://gist.github.com/)
2. Вставьте ссылку в нужную графу в [Гуглодок с решениями](https://docs.google.com/spreadsheet/ccc?key=0AtJr69JHs0W0dDJ0Q2FPcktLZjhnOTNIdndyV2VtWHc#gid=1)


Задачи
------

1. Пользователь вводит строку. Посчитайте количество различных слов в ней.
2. Пользователь вводит имя файла. Посчитайте, сколько раз в нём встречается каждое его слово. Сделайте это за линейное время. Протестируйте на любом отрывке из Википедии.
3. [Напишите функцию compress](https://gist.github.com/vpavlenko/5990e5daa1bcab8e3b2a)
6. [Объектно-ориентированное программирование](oop)
3. [Подсчёты на файле с данными](https://github.com/vpavlenko/python-for-ml-tasks)
5. [Регулярные выражения](https://github.com/vpavlenko/regexp-task/)
1. [Парсим HTML через BeautifulSoup](parse_html)
2. [Получаем страницы из интернета через requests](wget)
3. [Делаем запросы к JSON API](api)
3. [Делаем поиск по файлам](ack)
10. [Вызываем стороннее приложение, пишем HTTP-сервер](server)


Материалы
-------------------
3. [Пример: текущая директория и директория скрипта](paths)
1. [Менеджеры контекста, доктесты, функциональщина](http://vpavlenko.github.io/startup-engineering/python-bis/dark_magic/)
2. [Конспекты в интерактивном учебнике](http://pythontutor.ru/)
3. [Минитест по Питону](https://docs.google.com/document/d/1j6pm1T_HIfwup8vp09ZEhgoLBkiW4HBX_GL1VUQC3_k/)
3. Марк Саммерфилд. Программирование на Python 3
