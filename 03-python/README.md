Python
======================

Что нужно установить
--------

Установите Python3, setuptools и pip. При желании также установите текстовый редактор [Sublime Text](http://www.sublimetext.com/) и среду разработки [PyCharm](http://www.jetbrains.com/pycharm/).

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
1. [Арифметика, списки, строки, множества, словари, if, for](python_examples.py) ([pythontutor](http://gg.gg/se_tutor_1))
2. [Словари, срезы](python_examples_2.py) ([pythontutor](http://gg.gg/se_tutor_2))
3. [min/max, функции, lambda](python_examples_3.py) ([pythontutor](http://gg.gg/se_tutor_3_v2))
3. [Файловый ввод-вывод](http://contest.mccme.ru/pylernu/courses/1534/lessons/file_io/)
3. [Пример: текущая директория и директория скрипта](paths)
6. [Объектно-ориентированное программирование](oop)


Как сдавать решения
-------------------

1. Залейте решение на [gist.github.com](https://gist.github.com/) или на [pastebin.com](http://pastebin.com/)
2. Вставьте ссылку в нужную графу в [Гуглодок с решениями](https://docs.google.com/spreadsheet/ccc?key=0AtJr69JHs0W0dHBtaExsZDR3TkpjaHphbTcwYmpLX3c&usp=sharing#gid=1)


Задачи
------

1. Пользователь вводит строку. Посчитайте количество различных слов в ней.
2. Пользователь вводит имя файла. Посчитайте, сколько раз в нём встречается каждое его слово. Сделайте это за линейное время.
3. [Общеукрепляющее, задания 1-4](https://github.com/vpavlenko/python-for-ml-tasks)
5. [Регулярные выражения, задания 1 и 2](https://github.com/vpavlenko/regexp-task/)
1. [Парсим HTML через BeautifulSoup](parse_html)
2. [Получаем страницы из интернета через requests](wget)
3. [Делаем запросы к JSON API](api)
3. [Делаем поиск по файлам](ack)
10. [Вызываем стороннее приложение, пишем HTTP-сервер](server)


Материалы
-------------------
1. [Менеджеры контекста, доктесты, функциональщина](http://vpavlenko.github.io/startup-engineering/python-bis/dark_magic/)
2. [Конспекты в интерактивном учебнике](http://pythontutor.ru/)
3. Марк Саммерфилд. Программирование на Python 3
