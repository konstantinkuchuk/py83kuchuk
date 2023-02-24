# однострочный комментарий
"""
многострочный комментарий

"""
'''
многострочный комментарий
'''
# базовые типы данных
# 1 string str строки 'hello' "world"
# 2 integer int числа -5  6 123
# 3 float вещественные числа 8.23 3.14 - 6.23
# 4 boolean bool True 1 /False 0
# динамическая типизация
# age = 25  # присваивание
# name = 'Max'
# print('name:', name, 'age:', age)
# не называем ключевыми словами print type if for else
# не начианем с цифры 1_home
# нельзя использовать бинарные символы @+-%*&~,
# нельзя использовать руссие буквы
# # + - * **(возведение в степень) /(обычное деление) //(целочисленное деление) %(деление с остатком)
# number_1 = 9
# number_2 = 3.2
# result = number_1 / number_2
# print(round(number_2))

# print(some_string + " " + "world")# конкатенация
# print(some_string + str(5))

# numb = int(some_string)
# print(type(numb))
# some_string = "314" # пустая строка
# numb = 0
# logik = bool(some_string)
# some_float = float(some_string)
# print(some_float)
# age = int(input("enter age:"))
# name = input("enter name:")
# print(age - 2)
# print(name)
# x = int(input("enter x:"))
# y = int(input("enter y:"))
# res = (x + y) ** 23 * 2 - 5 + (x / y)
# print(res)
# 13. Дана длина ребра куба.
# Найти площадь грани, площадь полной поверхности и объем куба
# length_cube = float(input('enter length:'))
# length_power_2 = length_cube**2
# print(length_power_2)
# print(length_power_2 * 6)
# print(length_cube ** 3)
# number = 451
# x = number // 100
# y = number % 100 // 10
# c = number % 10
# number2 = c * 100 + y * 10 + x
# print(number2)
# number = 10
# print('number:',number)
# seconds = int(input('enter seconds:'))
# var1, var2 = input(), input()
# print(var1, var2)
# var1, var2, var3 = map(str, input("enter variables:").split())
# print('var1:', var1)
# print('var2:', var2)
# print('var3:', var3)
# a = 150
# b = 25
# print(a * b // 900)

# var1 = 5
# var2 = 4
# print(var1, var2)
# temp = var1
# var1 = var2
# var2 = temp
# var1, var2 = var2, var1
# print(var1, var2)
# логические выражение(boolean)
# >(больше) >= (больше или равно) <(меньше) <= (меньше или равно)
# != (не равно) == (равно) is (есть)
# and(и) or (или) not(не) xor(одно или)
# var1 = 'hello world'
# var2 = 'hello world'.lower()
# print(var1)
# print(var2)
# print(id(var1),id(var2))
# print(var1 is var2)
# print(5 == 5 and 6 > 3)
# print(not (5 == 7) or 6 > 13)
# print(18 % 2 == 0)
# if eсли else иначе
# number = int(input('enter number:'))
# if number > 0:  # условие ? True/False
#     # тело условного оператора
#     print('positive')
#     number += 2 # -= *= /= //= %= **=
#     if 10 <= number < 100:
#         print("двузначное")
#     else:
#         print('не двузначное')
#
# elif number == 0:
#     print('zero')
# else:
#     print('negative')
#     print(number - 2)
#
# print("end program")
# season = input('enter season of year')
# print(repr(season))
# if season == 'winter':
#  print('winter is here')
# elif season == 'autumn':
#     print('autumn is here')
# elif season == 'spring':
#     print('spring is here')
# elif season == 'summer':
#     print('summer is here')
# else:
#     print('unknown season')
# a, b, c = map(int, input("enter lines of triangle:").split())
# if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0:
#     if a == b == c:
#         print('равносторонний')
#     elif a == b or a == c or b == c:
#         print('равнобедренный')
#     else:
#         print('разносторонний')
# else:
#     print("не существует")

# var1 = 10
# var2 = 2
# exp = var1 > var2
# print(exp)
# if exp:
#     print(var1)
# тернарный оператор
# что написать if условие верно else что наисать
# number = int(input())
# print('чётное' if number % 2 == 0 else "нечётное")
# строки str '' ""
# \n перенос курсора \t табуляция \a перенос курсора в начало строки
# some_str = """
# hello world
# I learn python
# """
# some_str = some_str.replace('\n',' ')
# print(repr(some_str))
# str_1 = 'hello'
# str_2 = 'world'
# print(str_1 * 3)
#       012345678910
# name = 'John Watson'
# numb = name.find('z')
# numb = name.index('z')
# print(id(name))
# name = name.strip()
# print(id(name))
# if age.isdigit():
#     age = int(age)
#     print(age)
# else:
#     print('age is not a digit')
# slice (срез) str[start:end:step] str[start:end] str[::step]
# print(name[:4])
# print(name[5:])
# print(name[1:4])
# print(name[3:0:-1])
# print(name[::2])
# print(name[::-1])
# print(name[:2] + name[5:8])
# s = ' '
# print(ord(s))
# name1 = 'John'
# name2 = 'Jit'
# print(name1 > name2)
# 3.	Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
# name = "John Watson"
# str1 = name[:4]
# str2 = name[5:]
# name2 = str2 + " " + str1
# print(name2)
# str1 = "192.168.0.1"
# print(str1.replace('.', ' '))
# print(int(str1[0:3]) + int(str1[4:7]) + int(str1[8]) + int(str1[10]))
# x = int(input())
# y = int(input())
# print((x // 30) * (y // 30))

# seconds = int(input())
# hours = seconds // 3600 % 24
# minutes = (seconds - (hours * 3600)) // 60
# seconds = seconds - (hours * 3600) - minutes * 60
# print(hours, minutes, seconds)
# money = int(input())
# m100 = money // 100
# m50 = money % 100 // 50
# m10 = money % 100 % 50 // 10
# m1 = money % 10
# print(m100, m50, m10, m1)
# print(0**0)

# h = int(input('количество метров:'))
# day = int(input('расстояние за день:'))
# night = int(input('расстояние за ночь:'))
# h = h - day
# day_travel = day - night
# print((h - 1) / day_travel + 1 + 1)
# length = 56
# speed = int(input('введите скорость км/ч:'))
# hours = int(input('введите часы:'))
# minutes = int(input('введите минуты:'))
# time_trevel = hours + minutes / 60
# trevel_dist = time_trevel * speed
# print(time_trevel)
# print(trevel_dist)
# print(trevel_dist % length )
# print(-8 % 6)
# number = input()
# print(int(number[-1]) == 3)
# numb1, numb2 = map(int, input('введите 2 числа').split())
# print(numb1 % 2 == numb2 % 2)
# KISS keep it simple stupid
# numb1, numb2, numb3 = map(int, input('введите 2 числа').split())
# counter = 0
# if numb1 % 2 == 0:
#     counter = counter + 1
# if numb2 % 2 == 0:
#     counter = counter + 1
# if numb3 % 2 == 0:
#     counter = counter + 1
# print(counter)
# найти максимальное из 3 чисел
# numb1, numb2, numb3 = map(int, input('введите 3 числа').split())
# max_el = numb1
# if max_el < numb2:
#     max_el = numb2
# if max_el < numb3:
#     max_el = numb3
# print(max_el)
# 7)Дано четырёхзначное число. Проверить, одинаковы ли все цифры в нём.
# number = int(input())
# print(number % 1111 == 0)
# print(str(number)[0] == str(number)[1] == str(number)[2] == str(number)[3])
# year = int(input())
# # print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# s = input()
# print(s == s[::-1])
# s = input()
# count_f = s.count('f')
# if count_f == 1:
#     print(-1)
# elif count_f == 0:
#     print(-2)
# else:
#     first_ind = s.find('f')
#     second_ind = s.find('f', first_ind + 1)
#     third_ind = s.find('f', second_ind + 1)
# s = input().lower()
# count_g = s.count('g')
# count_c = s.count('c')
# length = len(s)
# print((count_c+count_g)/length * 100)
# циклы (повторение)
# цикл с параметром( цикл перебора объектов) for
# цикл с условием
# for var in (итерируемый объект)
# range(start,stop,step)
# range(1,5,1) 1 2 3 4
# range(1,5) 1 2 3 4 # если шаг равен 1 можно не писать
# range(5) 0 1 2 3 4
# for elem in range(10,0,-1):
#     print(elem,end=" ")
#    012345678910
# s = "hello world"
# # перебор строки по элементам
# for symb in s:
#     print(symb,end=" ")
# print()
# # перебор строки по индексам
# for ind in range(len(s)):
#     print(ind,s[ind])
# все числа кратные 5 на промежутке 1 до 100
# for numb in range(1, 101):
#     if numb % 5 == 0:
#         print(numb**2, end=" ")
# найти сумму всех чисел на промежутке от 10 до 50
# summa = 0
# for numb in range(10,51):
#     summa += numb
#
# print(summa)

# дано число, вывести все его делители
# 10 1 2 5 10
# 12 1 2 3 4 6 12
# number = int(input())
# for numb in range(1, number + 1):
#     if number % numb == 0:
#         print(numb, end=" ")
# range(start,stop,step)
# for number in range(12, -8, -1):
#     if number % 2 == 0:
#         print(number,end=' ')
# s = 'hello world'
# for symb in s:
#     print(symb)
# s = s[::-1]
# for ind in range(len(s)):
#     print(ind, s[ind])
# цикл с условие

# while True - бесконечный цикл
# break досрочно прерывает цикл
# count_dish = 0
# while True:# True/False
#
#     answer = input("Введите есть ли посуда(да/нет):")
#     if answer == "нет":
#         break
#     print('берём тарелку, моем, сушим')
#     count_dish += 1
#
# print('мы вымыли ', count_dish, 'тарелки')
# if count_dish != 0:
#     print('отдыхаем после мытья')
# else:
#     print('кто-то за нас помыл посуду?')
# вывести все числа от 1 до n c помощью while
# n = int(input('Введите конечное число'))
# begin = 1
# while begin <= n:
#     print(begin, end=" ")
#     begin += 1
# print('\nциел завершён')
# for i in range(begin, n + 1):
#     print(i, end=" ")
# статистика рождаемости

# count_babies = 0
# count_days = 0
# while True:
#     stat = int(input("введите количество новорожденных в день:"))
#
#     if stat == 0:
#         break
#
#     if stat > 10:
#         continue
#     count_days += 1
#     count_babies += stat
#
# print('количество новорожденых:', count_babies)
# print('количество дней работы:', count_days)
# дано число - вывести все его цифры
# number = int(input("введите число")[::-1])
# while number != 0:
#     n = number % 10
#     print(n)
#     number = number // 10

# дано число - вывести все его цифры
# number = input("введите число") # 51261251
# summa = 0
# for n in "51261251":
#     summa += int(n)
# print(summa)
# найти нод 2 чисел наибольший общий делитель

# numb, numb2 = map(int, input().split())
# numb = abs(numb)
# numb2 = abs(numb2)
# numbers = 1# 1 .. numb, numb2
# nod = 1
# while True:
#     if numb % numbers == 0 and numb2 % numbers == 0:
#         nod = numbers
#     numbers += 1
#     if numbers > numb or numbers > numb2:
#         print('nod is', nod)
#         break
# строки - не изменяема
#    012345678910
# len(s) = 11

# for ind in range(len(s)):
#     if ind == len(s) - 2:
#         temp += s[ind].upper()
#         continue
#     temp += s[ind]
#     print(ind)
# print(temp)
# in в
# not in не в
# print('o' not in 'hell')
# s = 'hello world'
# gl = 'aeyuioAEYUIO'
# temp = ""
# print(len(s))
# for ind in range(len(s)):# 0 1 2 3 .. 10
#     print(s[ind])
#     if s[ind] in gl:
#         temp += s[ind]
# print(temp)
# text = "dog    cat      frog     mouse" + " "
# temp = ""
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp:  # если строка существует(она не пустая)
#         print(temp)
#         # temp = ""
# 21.	Дана текст  text и символ c. Все слова в тексте разделены
# одним или несколькими пробелами. Написать программу определяющую
# количество слов текста, в которых содержится заданный символ, и вывести все слова
# text = "dog    cat      frog     mouse" + " "
# temp = ""
# letter = 'o'
# count = 0
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp:  # если строка существует(она не пустая)
#         if letter in temp:
#             print(temp)
#             count += 1
#         temp = ""
# print(count)
# name = 'Jhon'
# age = 45
# print(f"name: {name} age: {age}")
# print('name:', name, 'age:', age)
# форматированные строки
# print("name: {} age: {}".format(name, age))
# f-string f - нотации
# вывод строки через спецификаторы
# %s - string
# %f - float
# %d - int
# print("name: %s age: %d" % (name, age))
# (int,float) string
# number = int(input("enter number:"))
# count = 0
# # numb 1 .. 11
# for numb in range(1, number + 1):
#     if number % numb == 0:
#         count += 1
#         print(numb)
# if count == 2:
#     print('простое')
# else:
#     print("не простое")

# 7.	Найти произведение всех целых чисел от 5 до 20 включительно.
# mult = 1
# for i in range(5,100):
#     mult *= i
# print(mult)
# cows = int(input("enter count of cow:"))
# for cow in range(1, cows + 1):
#     if cow % 10 == 1 and cow % 100 != 11:
#         print(f"{cow} корова")
# 11.Даны натуральные числа n, m. Получить все числа меньше m взаимно простые с n.
# взаимно простые числа - числа с nod = 1 (4,5) (12,29) (15 16)
# n, m = map(int, input("enter n,m").split())
# for numb in range(2, m + 1):
#     temp_numb = numb
#     temp_n = n
#     while temp_numb != 0 and temp_n != 0:
#         if temp_numb > temp_n:
#             temp_numb %= temp_n
#         else:
#             temp_n %= temp_numb
#     if temp_n + temp_numb == 1:
#         print(f"{numb} is simpe with {n}")
# 3.	Дано натуральное число. Определить
# произведение цифр в нем которые кратны 2, кроме числа 0.

# print(bool(10))
# 120456
# mult = 1
# while numb:
#     if numb % 10 % 2 == 0 and numb % 10 != 0:
#         mult *= numb % 10
#     numb //= 10
# print(mult)
# 5.	Дано число n. Среди чисел 1, 4, 9, 16, 25, найти первое, которые больше n.
# KISS
# numb = 1
# n = int(input())
# temp = numb ** 2
# while temp < n:
#     numb += 1
#     temp = numb ** 2
# print(temp)
# 6.	Дано число n. Определить первую цифру этого числа.
# n = abs(int(input()))
# while n > 9:
#     n //= 10
# print(n)
# 8.Дано натуральное число n. Найти значение минимальной цифры в данном числе.
# number = int(input())
# min_num = number % 10
# while number:
#     if min_num > number % 10:
#         min_num = number % 10
#     number //= 10
# print(min_num)
# tuple(кортежи) unmutable
#        -6     -5    -4   -3   -2       -1
#         0      1    2    3    4         5
# tup = ('hello', 54, True, 5.23, 54, (1, 2, 5))
# перебор по элементам
# for elem in tup:
#     print(elem)
# # перебор по индексам
# for ind in range(len(tup)):
#     print(tup[ind])
# tup2 = (1, 4, 5)
# tup += tup2
# print(tup)
# print(id(tup))
# print(tup.index(55))
# s = 'hello'
# tup = tuple(s.split())
# print(tup)
# tup = (5, 6, 1, 10, 18, 5, 2)
# # найти максимальный элемент
# max_el = tup[0]
# for elem in tup:
#     if elem > max_el:
#         max_el = elem
# print(max_el)

# list (списки) mutable(изменяемые)
#      0    1  2      3     4        5          6
# lst = [5, 2.42, 5, 'hello', True, (6, 1, 2), [5, 2, 9]]
# tup = (5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9])
# print(lst.__sizeof__())
# print(tup.__sizeof__())
# lst += "hello"
# lst.append([5.23,4,2])
# lst.insert(2, [6,2,5])
# if 15 in lst:
#     lst.remove(15)
# del lst[3:10]
# lst.pop(10)
# print(lst[1:5])
# lst.clear()
# lst.extend("hello")
# lst += [5,2,5]
# print(lst.count(5))
# lst2 = lst[:]
#
# lst2.remove(5)
# print(lst2)
# # print(lst)
# s = "hello"
# lst =list([4,5,2])
# print(lst)
# lst = []
# n = int(input("enter count of elem:"))
# for i in range(n):
#     elem = int(input('enter elem:'))
#     lst.append(elem)
# print(lst)
# list comprehension
# 1 [что хотим добавить for из чего хотим доваить in итерабельный объект]
# 2 [что хотим добавить for из чего хотим доваить in итерабельный объект if условие верно]
# 3 [что хотим добавит if условие верно else что хотим добавить for из чего хотим доваить in итерабельный объект]
# print("чётное" if 4 %2 ==0 else "нечётное")
# print([numb.upper() for numb in "Hello"])
# print([numb**3 for numb in range(1,11)])
# print([numb for numb in range(1,11) if numb**2 % 3 == 0])
# print([symb for symb in "Hello" if symb in "AEYUIOaeyuio"])
# print([numb if numb % 2 == 0 else numb ** 2 for numb in range(1, 11)])
# print([int(input()) for i in range(5)])
# print([int(i) for i in input().split()])
# s = "hello world i am Piter Parker"
# lst = s.split()
# lst = [elem for elem in lst if elem[0].islower()]
# s = " ".join(lst)
# print(s)
# some_str = input('Код ДНК:')
# some_str = some_str.lower()
# temp = ''
# counter = 1
# for ind in range(len(some_str)):
#     temp += some_str[ind]
#     if ind == len(some_str) - 1 and temp[-1] == temp[-2]:
#         temp = temp[0: len(temp) - 1 - counter + 1]
#         temp += str(counter + 1)
#     elif ind == len(some_str) - 1 and temp[-1] != temp[-2]:
#         temp = temp[0: len(temp) - 1 - counter + 1]
#         temp += str(counter) + some_str[ind] + '1'
#     elif len(temp) > 1 and temp[-1] == temp[-2]:
#         counter += 1
#     elif len(temp) > 1 and temp[-1] != temp[-2]:
#         temp = temp[0: len(temp) - 1 - counter + 1]
#         temp += str(counter) + some_str[ind]
#         counter = 1
# print(temp)
# 3.	Удалить в строке все буквы 'b', непосредственно за которыми идет цифра.
# s = input() + " "
# temp = ""
# for i in range(len(s)):
#     if s[i] == 'b' and s[i+1].isdigit():
#         continue
#     temp += s[i]
# print(s)
# print(temp)
# print('hello world  '.capitalize().upper().rstrip())
# 4.	Дан текст. Слова в тексте разделены одним или несколькими пробелами.
# Написать программу определяющую количество слов,
# заканчивающихся одной и той же буквой ‘k’.

# print(lst)
# print(len([elem for elem in s.split() if elem[-1] == 'k']))
# count = 0
# for elem in lst:
#     if elem[-1] == 'k':
#         count += 1
# print(count)
# s = 'fqwfqwfq  d   dqwdk dkqwdqwd     kqwdqwk    dqwdk d qw qdwdqk' + " "
# temp = ""
# count = 0
# for ind in range(len(s)):
#     if s[ind] == 'k' and s[ind+1] == " ":
#         count += 1
# print(count)
# print(len([s[ind] for ind in range(len(s)) if s[ind] == 'k' and s[ind + 1] == " "]))

# Sample Input 1:
# 0 1 2 3 4
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7

# lst = [int(i) for i in input().split()]
# lst2 = []
# if len(lst) == 1:
#     print(lst)
# else:
#     for i in range(len(lst)):  # 0 1 2 3 4
#         if i == 0:
#             lst2.append(lst[-1] + lst[1])
#         elif i == len(lst) - 1:
#             lst2.append(lst[-2] + lst[0])
#         else:
#             lst2.append(lst[i - 1] + lst[i + 1])
#     print(lst2)
# 7.Дан список, упорядоченный по не убыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# lst1 = [1, 2, 2, 2, 6, 7, 10, 10, 12]
# lst1 = [1, 1, 1, 1, 1, 1, 1, 1]
# lst2 = []
# for elem in lst1:
#     print(elem, end=" ")
# for ind, elem in enumerate(lst1):
#     print(ind, elem)
# for ind in range(len(lst1)):
#     if lst1[ind] not in lst2:
#         lst2.append(lst1[ind])
# print(len(lst2))
# count = 1
# # for ind, elem in enumerate(lst1):
# #     if elem < lst1[ind + 1] and ind < len(lst1) - 1:
# #         count += 1
# # print(count)
# # for i in range(len(lst1) - 1):
# #     if lst1[i] < lst1[i + 1]:
# #         count += 1
# # # if lst1[-2] < lst1[-1]:
# count = 1
# print(count)
# ind = 0
# while ind < len(lst1):
#     if ind == len(lst1)-2:
#         if lst1[ind] < lst1[ind + 1]:
#             count += 1
#         break
#     if lst1[ind] < lst1[ind + 1]:
#         count += 1
#     ind += 1
#
# print(count)
# number = int(input())
# count = 0
# summa = 0
# while number != 0:
#     summa += number
#     count += 1
#     number = int(input())
#     if number > 10:
#         break
#     if number < 0:
#         break
# else:
#     print('break не исполнился')
#     print(count)
#
# print(summa)
# print(count)
# str list
# множества замореженное множество

# set_1 = {5,  5, 2, 2, 4, 'hello', 'hello', 4.22, (4, 2, 1),True}
# print(set_1)
# set_1.add(4)
# set_1.update([7,3,1])
# for elem in set_1:
#     print(elem)
# # set_1.update("home".split())
# set_1.pop()
# var = set_1.pop()
# print(var)
# set_1.discard(5)
# set_1.discard(5)
# set_1.remove(5)
# if 5 in set_1:
#     set_1.remove(5)
# set_1.clear()
# set_1.
# print(set_1)
# set_1 = {2, 6, 7, 9}
# set_2 = {2, 3, 6, 7, 11}
# print(set_1.issubset(set_2))
# print(set_2.issuperset(set_1))
# set_1.update(set_2)
# set_1.intersection_update(set_2)
# print(set_2.difference(set_1))
# print(set_1.symmetric_difference(set_2))
# print(set_2)
# set1 = {4, 2, 1, 5}
# f_set1 = frozenset(set1)
# for elem in f_set1:
#     print(elem)
# 3.	Даны два списка чисел. Найдите все числа,
# которые не содержатся одновременно в этих двух списках.
# lst = [5, 2, 6, 1, 2, 5, 2]
# lst_2 = [5, 2, 5, 1, 2, 9]
# set1 = set(lst)
# set2 = set(lst_2)
# print(set1.symmetric_difference(set2))

# словари dict (key : value) ассоциативный массив
#          key      value
#  key unique unmutable(неизменяемы)
# key - str int float bool tuple
# value - любой могут повторятся
# friend_phones = {"Vasya": 321748721, 'Anna': 12421412, "Pavel": 421512}
# for friend in friend_phones:
#     print(friend, friend_phones[friend])
# for friend, phone in friend_phones.items():
#     print(friend,phone)
# for phone in friend_phones.values():
#     print(phone)
# friend_phones["Angelina"] = 12421412
# friend_phones["Vasya"] = 21412512
# print(friend_phones)
# if "Paul" not in friend_phones:
#     friend_phones.update({"Paul": int(input())})
# print(friend_phones)
# friend_phones.pop("Vasya")
# friend_phones = friend_phones.fromkeys([5, 2, 6, 8], 42)
# print(friend_phones["Vasya"])


# МНОЖЕСТВА
# ЗАМОРОЖЕННОЕ МНОЖЕСТВО
# set_1 = {5, 5, 3, 2, 3, 4, 'hello','hello', (4, 2, 1)}
#
# print(set_1)
# set_1.update([7, 3, 1])
# for elem in set_1:
#     print(elem)
# set_1.update((4,2,1,9))
# var = set_1.pop()
# print(var)
# set_1.discard(5)
# set_1.remove(5)
# if 5 in set_1:
#     set_1.remove(5)
# print(set_1)

# set_1 = {2, 6, 7}
# set_2 = {2, 3, 6, 7, 11}
# # set_1.update(set_2)
# # print(set_1.intersection_update(set_2))
# # print(set_1.difference(set_2))
# # print(set_1.symmetric_difference(set_2))
# # print(set_1.issubset(set_2))
# # print(set_2.issuperset(set_1))

# lst = [5, 2, 6, 1, 2, 5, 2]
# lst_2 = [5, 2, 5, 1, 2, 9]
# set1 = set(lst)
# set2 = set(lst_2)
# print(set1.symmetric_difference(set2))


# f_set1 = frozenset(set_1)
# print(f_set1)

# CЛОВАРИ dict (key : value) ассоциативный массив
#           key       value
# key unique unmutable (неизм)
# key - str int float bool tuple
# value - любой тип данных
#
# friends_phones = {"vasya":321654525, "anna":8946598465, "pavel":8945121651}
# # for friend in friends_phones:
# #     print(friend, friends_phones[friend])
# # for friend,phone in friends_phones.items():
# #     print(friend,phone)
# # for phone in friends_phones.values():
# #     print(phone)
# # friends_phones["angelina"] = 4654165135
# print(friends_phones)
#

# ДЗ НА КОРТЕЖИ
# # 1
# tpl = (6, 2, 7, 8)
# print(tpl[0])
#
# # 2
# tpl = (12, 4, 67, 3)
# max_numb = max(tpl)
# min_numb = min(tpl)
# i = max_numb - min_numb
# print(i)

# # 3
# tpl = (5, 2, -2, 7, -8, -9, 1)
# count = 0
# for i in range(len(tpl) - 1):
#     if (tpl[i] > 0 and tpl[i + 1] < 0) or (tpl[i] < 0 and tpl[i + 1] > 0):
#         count += 1
# print(count)

# #4
# tpl = (4, 13, 17, 15, 20)
# lst = []
# k = 0
# for i in tpl:
#     for j in range(2, i):
#         if i % j == 0:
#             k = k + 1
#     if k == 0:
#         lst.append(i)
#     else:
#         k = 0
# print(lst)

# ДЗ НА СПИСКИ
# #1
# lst = [52, 75, 46, 67]
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i])

# #2
# lst1 = [2, 3, 5, 9]
# lst2 = [4, 3, 5, 10]
# for i in lst1:
#     if i not in lst2:
#         print(i)

# #3
# lst = [10, 1, 4, 6, 5, 9, 3]
# counter = 0
# for i in lst:
#     if i > i +1:
#         counter +=1
# print(i)

# #4
# lst = [45, 25, 72, 321]
# lst2 = " ".join(map(str, lst))
# lst3 = lst2[::-1]
# print(lst3)

# # 5
#
# lst1 = [2, 1, 3, 4, 2, 4, 4]
# lst2 = [x for x in lst1 if lst1.count(x) > 1]
# print(lst2)


# МНОЖЕСТВА
# #1
# lst = map(int, input().split())
# set1 = set()
# for i in lst:
#     if i in set1:
#         print('yes')
#     else:
#         print('no')
#         set1.add(i)

# # словари
# # 1
# school = {'9a': 20, '9b': 22, '9v': 19, '9m': 25, '9f': 20}
# school['9a'] = 17
# school['9g'] = 15
# school.pop('9f')
# print(school, (sum(school.values())))
#
# # 2
# slang = {'DNS': 'компьютерная система для получения, хранения и обработки информации о доменных именах',
#          'Интрасеть': 'это замкнутая внутренняя сеть какой- либо организации, работающая по Интернет- протоколу TCP/IP',
#          'Фича': 'Недокументированная дополнителоьная возможность, фишка',
#          'Мейнфрейм': 'большой компьютер, имеющий высокую вычислительную мощность'}
# while True:
#     raw = input()
#     raw2 = input()
#     raw3 = input()
#     raw4 = input()
#     if raw in slang:
#         print(slang[raw])
#     else:
#         print('Не найдено')
#     if raw2 in slang:
#         print(slang.raw2)
#     else:
#         print('Не найдено')
#     if raw3 in slang:
#         print(slang.raw3)
#     else:
#         print('Не найдено')
#     if raw4 in slang:
#         print(slang.raw4)
#     else:
#         print('Не найдено')
#     break


# МНОЖЕСТВА
# #1
# lst = map(int, input().split())
# set1 = set()
# for i in lst:
#     if i in set1:
#         print('yes')
#     else:
#         print('no')
#         set1.add(i)

# # словари
# # 1
# school = {'9a': 20, '9b': 22, '9v': 19, '9m': 25, '9f': 20}
# school['9a'] = 17
# school['9g'] = 15
# school.pop('9f')
# print(school, (sum(school.values())))

# # 2
# slang = {'DNS': 'компьютерная система для получения, хранения и обработки информации о доменных именах',
#          'Интрасеть': 'это замкнутая внутренняя сеть какой- либо организации, работающая по Интернет- протоколу TCP/IP',
#          'Фича': 'Недокументированная дополнителоьная возможность, фишка',
#          'Мейнфрейм': 'большой компьютер, имеющий высокую вычислительную мощность'}
# while True:
#     raw = input()
#     raw2 = input()
#     raw3 = input()
#     raw4 = input()
#     if raw in slang:
#         print(slang[raw])
#     else:
#         print('Не найдено')
#     if raw2 in slang:
#         print(slang[raw2])
#     else:
#         print('Не найдено')
#     if raw3 in slang:
#         print(slang[raw3])
#     else:
#         print('Не найдено')
#     if raw4 in slang:
#         print(slang[raw4])
#     else:
#         print('Не найдено')
#     break

# #3
# numb = {'ben': 123456789}
# strnumb = input().split()
# strnumb2 = input()
# if strnumb2 in numb:
#     print(numb[strnumb2])
# numb['add new name/number'] = strnumb
# print(numb)


# n = int(input())
# for i in range(1, n+1):
#     if i % 10 == 1 and i % 100 != 11:
#         print(f'{i} корова')
#     elif (i%10 == 2 and i%100 != 12) or (i%10 ==3 and i%100 !=13) or (i%100 != 14 and i%10 == 4):
#         print(f'{i} коровы')
#     else:
#         print(f'{i} коров')

# some_str = input().lower() + " "
# print(some_str)
# count = 1
# temp = ""
# for ind in range(len(some_str)-1):
#     if some_str[ind] == some_str[ind+1]:
#         count +=1
#     else:
#         temp +=some_str[ind] + str(count)
#         count = 1
# print(temp)




# ФУНКЦИИ
# алладин = global mainspace
# функция = лампа и джин
# реализация функции = 3 желания
# Алладин - лампа - джин - исполнял 3 желания - возвращался в лампу
# def show_lst():
#     for elem in lst:
#         print(elem)

# def pancakes():
#     print('взять ингридиенты (соль мука яйца молоко')
#     print('мешаем')
#     for i in range(5):
#         fried()
#         print(f'порция {i +1} готова')
#         print('==================')
#
# def fried():
#     print('наливаем на сковородку')
#     print('ждем 5 мин')
#     print('переворачиваем')
#     print('ждем 2 минуты')
#     print('выложить на тарелку и смазать')
#
# pancakes()


# def registr(name, age):
#     print(f'greeting {name} {age}')
# registr('oleg', 25)

# global scope
# # unmutable(неизм) в функцию передаются по значению
# name = 'vova'
# def greeting(name):
#     #процедура
#     # local scope
#     name = name.capitalize()
#     print(f'hello {name}')
#     return name
# name = greeting(name)
# print(name)
#
# greeting()


# #mutable передается в функцию
# people = ['Karl', 'vasya', 'petya']
# def workers():
#     people.append('Anna')
#     print(people)
# workers()


# # args - позиционные аргументы
# # balance =51000 аргументы переданые по ключу
# # **kwargs key word arguments
# def workers(date, *args, balance, balance_many=1000, **kwargs):
#     print(args)
#     print(balance)
#     print(date)
#     print(kwargs)
#     print(balance_many)
#
# workers('06.07.1997','vasya', 'petya', 'anna', balance = 510000, balance_many=999, balance1 = 421, balance2= 541, balance3 = 963)
#
# # def fun(*args, **kwargs): #обычно так будет


# # анонимные функции
# fun = lambda x, y: x + y
#
# def fun2(x,y):
#     return x+y
# # print(fun2(2,1))
# # print(fun(5,2))
# def chet(number):
#     return not number % 2
#
# lst = [5,2,6,1,7,8]
# # lst.sort(key=chet)
# # lst.sort(key=lambda numb: not numb % 2)
# print(lst)

# kr = lambda x: True if x % 3 == 0 else False
# # print(kr(6))
# lst = ['john', 'marry', 'jaccck']
# lst.sort(key =len)
# print(lst)

# # map
# lst = [5,2,5,1,7,2]
# balance = {'john':32541, 'Mark':74185, 'anna':12}
#
# for name in map(lambda name: balance[name]+20 if balance[name]<200 else balance[name], balance):
#     print(name, balance[name])

# #filter
# lst = [5,2,6,1,6,7,1]
# lst_2 = list(filter(lambda x: not x%2, lst))

# # words = ['hello', 'world', 'price', 'gold']
# # words2 = list(filter(lambda w: 'o' in w, words))
# # print(words2)
#
# words = ['hello', 'world', 'price', 'gold']
# words2 = list(filter(lambda w: len([sym for sym in w if sym in 'aeyuio']) == 2, words))
# print(words2)

# x = 2
# def fun():
#     global x
#     x+=3
#     print(x)
# fun()

# bgel
# global
# local
# enclosing
# built-it

# def fun(numb):
#     def wrapper():
#         nonlocal numb
#         numb +=1
#         print(numb)
#     wrapper()
# fun(42)


# closure
# def person(name):
#     def wrapper():
#         print(name.capitalize())
#     return wrapper
#
# p = person('oleg')
# p()

# def counter(x):
#     def wrapper(a):
#         nonlocal x
#         x += a
#         print(x)
#     return wrapper
# c = counter(0)
# c(1)
# c(1)
#
# def counter_2(x):
#     return x+1
# counter_2(1)
# counter_2(1)


# #ДЕКОРАТОР - ФУНКЦИЯ КОТОРАЯ ПРИНИМАЕТ ФУНКЦИЮ ЕЕ ЖЕ МОДЕРНИЗИРУЕТ И ВОЗВРАЩАЕТ
# def greeting(name: str):
#     return 'hello ' + name
#
#
# def decorator(fun):
#     def wrapper(name):
#         if name.capitalize() == name:
#             return fun(name)
#         else:
#             return 'hello' + name.capitalize()
#
#     return wrapper
# decor_say = decorator(greeting)
# # print(greeting('peter'))
# print(decor_say('peter'))


# users = {'john':1234, 'jack':590, 'anna':900}
# def balance (**kwargs):
#     for name,price in kwargs.items():
#         if price < 1000:
#             kwargs[name] +=100
#     return kwargs
# users = balance(**users)
# print(users)


# дз на функции
# 1
# def fib(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a,b = b, a+b
#
# fib2 = list(fib(10))
# print(fib2)


# def factor(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact = fact * i
#     return fact
# n = int(input())
# print(factor(n))

# #2
# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         return x + 5 - x % 5
# x = int(input())
# print(closest_mod_5(x))

# #3
# def check_variable():
#     a = input('1 Ввод: ')
#     b = input('2 Ввод: ')
#     c = input('3 Ввод: ')
#     if a.isdigit():
#         print('1- нельзя использовать')
#     else:
#         print('1- Можно использовать')
#     if b.isdigit():
#         print('2- нельзя использовать')
#     else:
#         print('1- Можно использовать')
#     if c.isdigit():
#         print('3- нельзя использовать')
#     else:
#         print('1- Можно использовать')
#     print('Поработали и хватит')
# check_variable()

# # 4
# def bank(a, y):
#     for i in range(y):
#         a = a + (a * 0.1)
#     return a
#
#
# a = int(input('Сумма: '))
# y = int(input('Лет: '))
# print(bank(a, y))

# #5 декораторы
# def decorator(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('Время выполнения: {} секунд.'.format(end-start))
#     return wrapper
#
# @decorator
# def say():
#     i = 1
#     while i < 101:
#         print(i, end=' ')
#         i+=1
# say()


# #6
# def decorator(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('время затраченное на регистрацию {} секунд.'.format(end-start))
#     return wrapper
#
# @decorator
# def registr():
#     surname = input('Введите фамилию: ')
#     name = input('Введите имя: ')
#     patronymic = input('Введите отчество: ')
#     return name, surname, patronymic
# registr()

# files
# режимы доступа
# w - write - запись()все,что было было, то пропало..
# r - read - чтение(считываем все из файла)
# a - append - дозапись(записывает в конец файла)
# x - запишет в файл инф если файла не существовало
# w+ r+ a+ wb rb ab xb wb+ rb+
####### file = open('test_file.txt', 'r', encoding='utf-8')
# # file.write(str(67)+ '\n')
# # some_str = file.read()
# lst = []
# for line in file:
#     lst.append(int(line.rstrip()))
# # some_str = file.readline()
# file.close()
# print(lst)
# # print(repr(some_str))
# # lst = some_str.replace('\n',' ').rstrip().split()
# # lst = list(map(int,lst))
# # print(lst)

# students = {}
# for line in file:
#     lst = line.rstrip().split()
#     marks = list(map(int,lst[1:]))
#     students[lst[0]] = marks
# file.close()
# print(students) не исправлено


# что такое контекст менеджер
# enter (входите) exit (выход)
# f= open('test_file.txt','r',encoding='UTF-8') as file:
#     lst = []
#     for line in file:
#         lst.extend(line.rstrip().split())
# max_len = 0
# number = 1
# s = ''
# for id, line in enumerate(lst):
#     if len(line) > max_len:
#         mex_len = len(line)
#         s = line
#         number = id + 1
# print(s)
# print(max_len)
# print(number)


#csv  comma separate values
# import random
# import csv
# lst = [str(random.randint(1,10) for _ in range(100))]
# # print(lst)
# # print(','.join(lst))
# # with open('test_csv.csv', 'w') as file_csv:
# #     file_csv.write(','.join(lst))
# with open('test_csv.csv', 'r') as file_csv_read:
#     s = csv.reader(file_csv_read)
#     print(s)
#     for el in s:
#         print(el)   не исправлено

# # json
# import json
# person = {
#     "name" : "john",
#     'lastname': "johnwatson",
#     "age": 24
#     }
# # dumps = cериализует объект
# with open('test_json.json','w',encoding='UTF-8') as file_json:
#     json.dump(person,file_json,indent=4)
#
# with open('test_json.json','r',encoding='UTF-8') as file_json_read:
#     person_2 = json.load(file_json_read)
#     print(person_2)




