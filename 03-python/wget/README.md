requests, BeautifulSoup, write to file, create folder
=====================================================

**Задача**. Считать из параметров запуска букву, скачать десять статей на эту букву с Urban Dictionary, положить в папку.

**Решение**. Используем библиотеку requests, которая позволяет выполнять HTTP-запросы.

    $ python script.py B
    ['Blowjob', 'boobs', 'Bootylicious', 'birthday', 'bush', 'bisexual', 'Bitch', 'Bromance', 'bed gravity', 'bored']
    Attempt to get http://www.urbandictionary.com/define.php?term=Blowjob
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=boobs
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=Bootylicious
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=birthday
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=bush
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=bisexual
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=Bitch
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=Bromance
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=bed gravity
    Success
    Attempt to get http://www.urbandictionary.com/define.php?term=bored
    Success

Задание
-------

Начиная со страницы http://www.siliconrus.com/, организуйте обход в глубину по ссылкам, скачивая по одной странице с одного домена, скачайте как минимум 100 страниц. Всё сохраните на диске.
