"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

"""
n = int(input("Введите количество монет: "))
from random import randint
coin = [randint(0, 1) for i in range(n)]
print(coin)
count = 0
for i in range(n):
    if coin[i] == 0:
        count += 1
if count <= n//2:
    print(count)        
else:
    print(n - count)    
"""

"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
"""
s = int(input("Введите сумму двух чисел: "))
p = int(input("Введите произведение двух чисел: "))
a = 1
b = -s
c = p
d = b**2 - 4*a*c
x1 = (-b - d**0.5)/(2*a)
x2 = (-b + d**0.5)/(2*a)
print(x1, x2)
"""

"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

n = int(input("Введите число n: "))
i = 0
while (2**i <= n):
    print(2**i)
    i += 1