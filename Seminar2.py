""" Задача No9. Решение в группах
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while
Input: 5
Output: 120 """
"""
n = int(input("Введите число: "))
f = 1
x = 1
while (x <= n):
    f = f * x
    x = x + 1
else:
    print(f)    
"""

""" Задача No11. Решение в группах
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое 
число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input: 5 Output: 6 """

"""
A = int(input("Введите число: "))

n = 0
n1 = 1
i = 2
t = 0
count = 0

while (A > count):
    count = n + n1
    t = n1
    n1 = n1 + n
    n = t
    if A == count:
        break
    i += 1
if count != A:
    print(-1)
else:
    print(i + 1)
"""


""" Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная
оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь,
занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в который среднесуточная температура
ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат 
в диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10 Output: 2 """

n = int(input("Введите количество дней"))
count = 0
max = 0
for i in range(n):
    x = int(input())
if x > 0:
    count += 1
else:
    if count>max:
        max = count
        count = 0
if count > max:
    max = count
print(max)

""" Задача No15.Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком 
много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой 
строчке каждое. Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9 Output: 1 9  """
"""
import random
n = int(input("Введите кол-во арбузов на рынке: "))
list = []
i = 0
for _ in range (n):
    list.append(random.randint(5, 20))
    max = list[i]
    min = list[i]
while n > i:
    if list[i] < min:
        min = list[i]
    if list[i] > max:
        max = list[i]
    i = i + 1
print(list)
print(f"Минимальный {min}, Максимальный {max}")
"""