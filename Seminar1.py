"""
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a < b:
    print(f" a = {a} меньше b")

elif a == b:
    print(f" a = {a} равно b")

else:
    print(f" a = {a} больше b")
    """

"""
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
n = 700 m = 750 Output: 2
"""
"""
n = 700
m = 700

print(round((m + n - 1)//n))
"""





"""
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для 
них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся
в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
"""

"""
a = int(input("Введите количество учащихся в первом классе: "))
b = int(input("Введите количество учащихся во втором классе: "))
c = int(input("Введите количество учащихся в третьем классе: "))

print(round(20/2 + 20 % 2) + round(21/2 + 21 % 2) + round(20/2 + 20 % 2))
"""
"""
a = int(input("Введите количество учащихся в первом классе: "))
b = int(input("Введите количество учащихся во втором классе: "))
c = int(input("Введите количество учащихся в третьем классе: "))
a1 = (a + 1) // 2
b1 = (b + 1) // 2
c1 = (c + 1) // 2
s = a1 + b1 + c1
print(s)
"""

"""
Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
(при этом иногда вагоны нумеруются от «головы» поезда, а иногда –  
с «хвоста»; это зависит от того, в какую сторону едет электричка). 
В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
Напишите программу, которая будет это делать или сообщать, что без дополнительной информации 
это сделать невозможно.
Input: 3 4(ввод на разных строках) Output: 6
"""
"""
x = int(input("Input i: "))
y = int(input("Input j: "))

if x == y:
    print('Need more information')
else:
    print(x + y - 1)    
"""

"""
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии 
с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100,
а также если он кратен 400.
Input: 2016 Output: YES
"""
"""
a = int(input("Введите год: "))
b = (a % 4)
c = a % 100
d = a % 400

if b == 0 and c != 0 or d == 0:
    print("Yes")
else:
    print("No")
"""