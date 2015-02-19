# язык Python за десять минут

# ввод-вывод cтрок
first_word = input()
second_word = input()
spell = first_word + ' ' + second_word + '!'
print(spell)

# ввод-вывод чисел
first_number = int(input())
second_number = float(input())
print(first_number + second_number)

# смешанный вывод чисел и строк
platform = first_number + second_number
print('Платформа №' + str(platform))
print('Платформа №', platform, sep='')

# числа
radius = 5
pi = 3.14159
square = pi * radius ** 2

# строки
s = 'Tom Marvolo Riddle'
tokens = s.split()
first_name = tokens[0]
middle_name = tokens[1]
last_name = tokens[2]
s2 = first_name + ' ' + middle_name + ' ' + last_name

# конструкция 'if'. важно ставить отступы!
if (s == s2):
    print('две строки равны')
else:
    print('так не бывает')

# списки (изменяемые последовательности)
houses = ['Ravenclaw', 'Hufflepuff', 'Gryffindor']
houses.append('Slytherin')
print(len(houses))

# цикл 'for'. отступы вновь важны!
for house in houses:
    print('Ten points to', house, end='!\n')

# set (неупорядоченные коллекции)
birth_name = 'Tom Marvolo Riddle'
birth_name_letters = set(birth_name)
birth_name_lower_letters = set(birth_name.lower())
nickname_lower_letters = set('I am Lord Voldemort'.lower())
print(birth_name_lower_letters == nickname_lower_letters)
print(len(birth_name_lower_letters))

fib_numbers = set([1, 1, 2, 3, 5, 8, 13, 21])
prime_numbers = set([2, 3, 5, 7, 11, 13, 17, 19])
union = fib_numbers | prime_numbers
intersection = fib_numbers & prime_numbers
difference = fib_numbers - prime_numbers
symmetric_difference = fib_numbers ^ prime_numbers

# проверка принадлежности
print(3 in prime_numbers)
print(4 in prime_numbers)
print('Griffindor' in houses)
print('ratio' in 'transfiguration')

# сортировка
houses.sort() # сортировка на месте
sorted_letters = sorted(houses[0]) # новый список
