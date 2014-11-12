iterate over directory, regexps, colorama
=========================================

**Задача.** Найти все строчки в файлах из данной директории, содержащие некоторую подстроку (или число, или электронный адрес). Вывести на терминал в разукрашенном виде.

**Решение.** Для раскраски используем модуль [colorama](https://pypi.python.org/pypi/colorama), для поиска - [регулярные выражения](http://docs.python.org/3.3/library/re.html).

    $ python script.py clicking
    engler
    597: obtained by clicking <a href="vcode-tutorial.ps">here</a>.  
    UnicodeDecodeError: file subh, line 110
    tim
    29: you can read the entire book online by clicking

Задание
-------

Добавьте в скрипт логику рекурсивного поиска по файловой системе, протестируйте её на вашем диске.
