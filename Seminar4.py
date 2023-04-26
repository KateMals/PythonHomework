# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки 
# на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1
"""
from random import randint
num = int(input("Введите количество оценок: "))
listOcenok = [randint(1, 5) for i in range(num)]
print(*listOcenok)

result = []
for element in listOcenok:
    if element == max(listOcenok):
        result.append(min(listOcenok))
    else:
        result.append(element)
print(*result)      
"""

# Написать функцию для факториала

"""
n = int(input("Введите положительное число: "))

def Factorial(n):
    if n == 0:
        return 1
    else:
        return Factorial(n - 1)*n
print(Factorial(n)) 
"""

#Задача No31. Общее обсуждение
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е 
"""
n = int(input("Введите число: "))

def Fib(n):
    if n == 0:
        return 0
    elif 1<= n <= 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
print(Fib(n))    
"""


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes
"""
n = int(input("Введите число: "))

def Simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(Simple(n))
"""

"""
n = int(input("Введите число: "))
i = n - 1

def Simple(n, i):
    if i == 1:
        return True
    else:
        if n % i == 0:
            return False
        return Simple(n, i - 1)
print(Simple(n, i)) 
"""

n = int(input("Введите число: "))
stroka = "3 4 6 8 9"

def revers(stroka):
    if len(stroka):
