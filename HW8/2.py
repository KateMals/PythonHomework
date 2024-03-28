# a = int(input())
# a3 = a % 100 // 10
# a4 = a % 10
# if a3 == a4 == 0:
#     print('YES')
# else:
#     print('NO')



# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if ((x1 + y1) % 2 == (x2 + y2) % 2) or ((x1 - x2) % 2 == (y1 - y2) % 2):
#     print("YES")
# else:
#     print("NO")


# age = int(input())
# sex = input()
# if (10 <= age <= 15) and (sex == 'f'):
#     print("YES")
# else:
#     print("NO")


# a = int(input())

# if a > 10 or a <= 0:
#     print('ошибка')
# elif a == 1:
#     print('I')
# elif a == 2:
#     print('II')
# elif a == 3:
#     print('III')
# elif a == 4:
#     print('IV')
# elif a == 5:
#     print('V')
# elif a == 6:
#     print('VI')
# elif a == 7:
#     print('VII')
# elif a == 8:
#     print('VIII')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')                   


# a = int(input())

# if a % 2 != 0:
#     print('YES')
# elif (a % 2 == 0) and (6 <= a <= 20):
#     print('YES')
# else:
#     print('NO')


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if ((x1 - x2) ** 2) == ((y1 - y2) ** 2):
#     print('YES')
# else:
#     print('NO')  

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if (((a - c) * (b - d)) == 2) or (((a - c) * (b - d)) == -2):
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if ((a - c) ** 2 == (b - d) ** 2) or a == c or b == d:
#     print('YES')
# else:
#     print('NO')



# a = float(input())
# b = float(input())

# print((a * b) / 2)


# S = float(input())
# V_1 = float(input())
# V_2 = float(input())

# print(S / (V_1 + V_2))


# a = float(input())

# if a == 0:
#     print('Обратного числа не существует')
# else:
#     print( a ** -1)    


# a = float(input())
# print((5 / 9) * (a - 32))




# a = float(input())
# a_1 = a * 10.5
# a_2 = 21 + (a - 2) * 4
# if a <= 2:
#     print(a_1)
# elif a > 2:
#     print(a_2)

        
# a = float(input())
# b = int(a * 10) % 10
# print(b)


# a = float(input())
# print(float(a - int(a)))


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# print('Наименьшее число =', min(a, b, c, d, e))
# print('Наибольшее число =', max(a, b, c, d, e))


# a = int(input())
# b = int(input())
# c = int(input())
# sum = a + b + c
# print(max(a, b, c))
# print(sum - min(a, b, c) - max(a, b, c))
# print(min(a, b, c))  


# a = int(input())
# a_1 = a // 100
# a_2 = a // 10 % 10
# a_3 = a % 10
# if (max(a_1, a_2, a_3) - min(a_1, a_2, a_3)) == ((a_1 + a_2 + a_3) - min(a_1, a_2, a_3) - max(a_1, a_2, a_3)):
#     print('Число интересное')
# else:
#     print('Число неинтересное')


# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(abs(a - c) + abs(b - d))

# a = '"Python is a great language!", said Fred. "I'
# b = " don't ever remember having this much fun before."
# c = '"'
# print(a + b + c)

# print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

# name = input()
# surname = input()
# print('"Hello', name, surname, '! You have just delved into Python"')


# name = input()
# print('Футбольная команда', name, 'имеет длину', len(name), 'символов')


# a = input()
# b = input()
# c = input()
# if (len(c) > len(a) < len(b)) and (len(a) < len(b) > len(c)):
#     mini = a
#     maxi = b
# elif (len(a) > len(b) < len(c)) and (len(a) < len(c) > len(b)):
#     mini = b
#     maxi = c
# elif (len(a) > len(c) < len(b)) and (len(c) < len(a) > len(b)):
#     mini = c
#     maxi = a

# print(mini)
# print(maxi) 


# a = input()
# b = input()
# c = input()
# if (len(b) == (len(a) + len(c)) / 2) or (len(a) == (len(b) + len(c)) / 2) or (len(c) == (len(a) + len(b)) / 2):
#     print('YES')
# else:
#     print('NO') 


# a = input()
# s = 'синий'
# if s in a:
#     print('YES')
# else:
#     print('NO')    


# a = input()
# if 'суббота' in a or 'воскресенье' in a:
#     print('YES')
# else:
#     print('NO')


# a = input()
# if '@' in a or '.' in a:
#     print('YES')
# else:
#     print('NO')

import math
from math import *



# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# print(sqrt((a - c) ** 2 + (b - d) ** 2))


# a = float(input())

# print(math.pi * (a ** 2))
# print(2 * math.pi * a)




# a = float(input())
# b = float(input())
# print((a + b) / 2)
# print(sqrt(a * b))
# print(((2 * a * b) / (a + b)))
# print(sqrt((a ** 2 + b ** 2) / 2))


# a = float(input())
# print((math.sin(math.radians(a)) + math.cos(math.radians(a)) + math.tan(math.radians(a)) ** 2))


# a = float(input())
# print(floor(a) + ceil(a))

import math
from math import *

# a = float(input())
# b = float(input())
# c = float(input())

# D = b ** 2 - 4 * a * c
# if D < 0:
#     print('Нет корней')
# elif D == 0:
#     x = - b / (2 * a)
#     print(x)
# elif D > 0:
#     x_1 = (- b + (sqrt(D))) / (2 * a)
#     x_2 = (- b - (sqrt(D))) / (2 * a)
#     print(min(x_1, x_2))
#     print(min(x_1, x_2))

# n = int(input())
# a = float(input())
# C = (n * (a **2)) / (4 * tan(pi / n))
# print(C)


n = int(input())
digit =  0
while n != 0:
    for i in range(0, n + 1, -1):
        digit = n % 10
        print(digit)
        n = n // 10
