# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
"""
n = int(input('Введите кол-во элементов 1-го множества: '))
m = int(input('Введите кол-во элементов 2-го множества: '))

first = set()
for i in range(n):
    first.add(int(input('Введите элемент 1-го множества: ')))
second = set()
for i in range(m):
    second.add(int(input('Введите элемент 2-го множества: ')))
result = first & second
AndResult = list(result)
AndResult.sort()
"""

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом заданной во входном файле грядки.


import random
n = int(input('Введите кол-во элементов кустов: '))
x = []

for i in range(n):
    x.append(random.randint(0,10))
print(x)

max = 0
sum = 0

for i in range(len(x)):
    sum = x[i - 2] + x[i - 1] + x[i]
    if sum > max:
        max = sum
print(max)