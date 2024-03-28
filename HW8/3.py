# for i in range(10):
#     print('Python is awesome!')


# x = input()
# y = int(input())
# for i in range(y):
#     print(x)


# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB') 
# print('E')
# for i in range(9):
#     print('TTTTT') 
# print('G')   


# x = int(input())
# for i in range(x):
#     print('*******************')

# x = input()
# for i in range(10):
#     print(i, x)


# x = int(input())
# for i in range(x + 1):
#     print('Квадрат числа', i, 'равен', i ** 2)


# x = int(input())
# for i in range(x):
#     print('*' * (x - i))


# m = float(input())
# p = float(input())
# n = int(input())

# for i in range(n):
#     print(i + 1, ( m * (1 + p / 100) ** i))

# for i in range(960, 1000):  # перебираем числа от 100 до 999
#     if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)  


# for i in range(56, 171):
#     if i % 10 == 0:
#         print(i)


# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     print(i)

# m = int(input())
# n = int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, - 1):
#         print(i)


# m = int(input())
# n = int(input())
# if m % 2 != 0:
#     for i in range(m, n, -2):
#         print(i)
# else:
#     for i in range(m - 1, n - 1, -2):
#         print(i)       


# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# n = int(input())
# for i in range(10):
#     print(n, 'x', i + 1, '=', n * (i + 1))

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end="")


# a = int(input())
# b = int(input())
# count = 0
# for i in range(a, b + 1):
#     if ((i ** 3) % 10 == 4) or ((i ** 3) % 10 == 9):
#         count = count + 1
# print(count)        


# n = int(input())
# sum = 0
# for i in range(n):
#     num = int(input())
#     sum = sum + num
# print(sum) 

# import math
# from math import *

# n = int(input())
# asimp = 1
# for i in range(2, n):
#     asimp = asimp + 1 /i
# print(asimp - log(n))    



# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if ((i ** 2) % 10 == 2) or ((i ** 2) % 10 == 5) or ((i ** 2) % 10 == 8):
#         count = count + 1
# print(count) 

# n = int(input())
# factorial = 1
# for i in range(n):
#     factorial = factorial * (i + 1)
# print(factorial)    


# proiz = 1
# for i in range(10):
#     num = int(input())
#     if num != 0:
#         proiz = proiz * num
# print(proiz)   



# n = int(input())
# divisors = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         divisors = divisors + i
# print(divisors)       


# n = int(input())
# znaksum = 0
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         znaksum = znaksum + i
#     elif i % 2 == 0:
#         znaksum = znaksum - i 
# print(znaksum)       



# n = int(input())
# num_1 = 0
# num_2 = 0
# sum = 0
# for i in range(n):
#     num = int(input())
# if num > num_1:
#     num_1 = num
# else:
#     num_2 = num    
# if num_1 > num_2:
#     num_1 = num_2
# else:
#     num_2 = num_1      
# print(num_2,num_1)


# chet = 0
# nechet = 0
# for i in range(10):    
#     n = int(input())
#     if n % 2 == 0:
#         chet = chet + 1
#     else:
#         nechet = nechet + 1
# if chet == 10:
#     print('YES')
# elif nechet == 10:
#     print('NO')        


# n = int(input())
# a = 1
# b = 2
# fib = 0
# if n == a:
#     print(a)
# elif n == 2:
#     print(a, a)
# else:    
#     for i in range(3, n):   
#         fib = (i - 1) + (i -2)
#     print(a, a, b , fib)   


# i = 0
# n = input()
# while n != 'КОНЕЦ':
#     print(n)
#     n = input()
#     i += 1


# i = 0
# n = input()
# while n != 'КОНЕЦ' and n != 'конец':
#     print(n)
#     n = input()
#     i += 1


# i = 0
# n = input()
# counter = 0
# while n != 'стоп' and n != 'хватит' and n != 'достаточно':
#     n = input()
#     counter = counter + 1
#     i += 1
# print(counter)    



# i = 0
# n = int(input())
# while (n % 7) == 0:
#     print(n)
#     n = int(input())
#     i += 1


# i = 0
# n = int(input())
# total = 0
# while n >= 0:
#     total = total + n
#     n = int(input())
#     i += 1
# print(total)  

# n = int(input())
# fives = 0
# while n > 0 and n <= 5:
#     if n == 5:
#         fives += 1
#     n = int(input())    
# print(fives)  


# sum = int(input())
# coins = int(1)
# if 2 <= sum < 5:
#     coins = int(sum / 1)
# elif 5 <= sum <= 9:
#     coins = sum // 5 + sum % 5
# elif 10 <= sum <= 24:
#     coins = sum // 10 + (sum % 10) // 5 + (sum % 10) // 1
# elif sum >= 25:
#     coins = sum // 25 + (sum % 25) // 10 + ((sum % 25) % 10) // 5 + (((sum % 25) % 10) % 5) // 1
# print(coins)


# n = int(input())
# digit =  0
# while n != 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10



# n = int(input())
# digit =  0
# while n != 0:
#     digit = n % 10
#     print(digit, end='')
#     n = n // 10


# n = int(input())
# digit = 0
# mini = 10
# maxi = 0
# while n!=0:
#     digit = n % 10
#     mini = min(digit, mini)
#     maxi = max(digit, maxi)
#     n = n // 10
# print('Максимальная цифра равна',maxi)
# print('Минимальная цифра равна',mini)


# n = int(input())
# digit = 0
# sum = 0
# counter = 0
# product = 1
# average = 0
# first = 0
# sum_1_2 = 0
# last_digit = n % 10
# while n != 0:
#     digit = n % 10
#     sum += digit
#     counter += 1
#     product *= digit
#     average = sum / counter
#     n = n // 10

# print(sum, counter, product, average, digit, digit + last_digit, sep='\n')



# n = int(input())
# digit = 0
# while n > 9:
#     digit = n % 10
#     n = n // 10
# print(digit)


# n = int(input())
# digit = 0
# result = 0
# counter = 0
# while n != 0:
#     digit = n % 10
#     counter += 1
#     n = n // 10 
#     if digit == (n % 10):
#         result += 1
# print(counter, result)
# if counter == result:
#     print('YES')   
# else:
#     print('NO')     


# n = int(input())
# prev_digit = n % 10
# n = n // 10
# flag = "YES"
# while n > 0:
#     digit = n % 10
#     if digit < prev_digit:
#         flag = "NO"
#     prev_digit = digit
#     n = n // 10
# print(flag)    


# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break


# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20


# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# n = int(input())
# min = 0
# for i in range(2, n + 1):
#     if n % i == 0:
#         break
# print(i)


# n = int(input())
# for i in range(1, n + 1):
#     if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
#         continue
#     print(i)


# for i in range(7, 101, 7):
#     print(i)

# count = 0
# p = 1
# for i in range(10):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# mx = 0
# s = 0
# count = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         mx = min(10**6, x)
#     if x > 0:
#         count += 1
# if count == 10:
#     print('NO')
# else:        
#     print(s)
#     print(mx)


# s = 0
# for i in range(7):
#     n = int(input())
#     if i % 2 == 0:
#         s = s + n
# print(s)


# n = int(input())
# max_digit = n % 10
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if (max_digit % 3) != 0:
#     print('NO')
# else:
#     print(max_digit)


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)


# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()

# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(9):
#         print(i + 1, '+',  j + 1, '=', i + 2 + j)
#     print()


# n = int(input())
# for i in range(1, n // 2 + 2):
#     print(i * '*')
# for j in range(n // 2, 0, -1):
#     print(j * '*')

# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(i + 1, end='')
#     print()


# for n in range(1, 365 // 28):
#     for k in range(1, 365 // 30):
#         for m in range(1, 365 // 31):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print("n =", n, "\nk =", k, "\nm =", m)
#                 print()

# for b in range(1, 100 // 10):
#     for k in range(1, 100 // 5):
#         for t in range(1, 200):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 print("n =", b, "\nk =", k, "\nm =", t)
#                 print()


# for a in range(1, 151):
#     for b in range(1, 151):
#         for c in range(1, 151):
#             for d in range(1, 151):
#                 for e in range(1, 151):
#                     if a <= b <= c <= d < e and (a ** 5 + b ** 5 + c ** 5 + d ** 5) == e ** 5:
#                         print(a, b, c, d, e)
#                     print()


# a = [i ** 5 for i in range(1, 151)]
# b = {}
# c = {}
# for i in range(150):
#     for j in range(i, 150):
#         c.setdefault(a[j] - a[i], []).append([j + 1, i + 1])
#         for k in range(j, 150):
#             b.setdefault(a[i] + a[j] + a[k], []).append([k + 1, j + 1, i + 1])

# lst = sorted(set(b.keys()) & set(c.keys()))
# res = sum(sum(c[lst[0]] + b[lst[0]], []))
# print(res)


# n = int(input())
# step = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(step, end=' ')
#         step += 1
#     print()  


# n = int(input())
# step = 1
# for i in range(1, n + 1):
#     print(step, end='')
#     step += 1
#     for j in range(i + 1, 0, -1):
#         print(step, end='') 
#     print()    


# import numpy as np 
# from statsmodels.stats.power import NormalIndPower 
# from statsmodels.stats.proportion import proportion_effectsize 
 
# # Задаем параметры 
# baseline_conversion = 0.05 
# expected_increase = 0.002 
# alpha = 0.03 
# power = 0.87 
# monthly_traffic = 40000 
 
# # Расчет эффекта 
# effect_size = proportion_effectsize(baseline_conversion, baseline_conversion + expected_increase) 
 
# # Создаем объект для расчета мощности 
# power_analysis = NormalIndPower() 
 
# # Расчет размера выборки на одну группу 
# sample_size_per_group = power_analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, ratio=1, alternative='smaller') 
 
# # Общий размер выборки для трех групп 
# total_sample_size = sample_size_per_group * 3 
 
# # Расчет количества дней для тестирования 
# days_required = total_sample_size / (monthly_traffic) 
 
# print(f"Размер выборки на одну группу: {np.ceil(sample_size_per_group)}") 
# print(f"Общий размер выборки для трех групп: {np.ceil(total_sample_size)}") 
# print(f"Необходимое количество дней для тестирования: {np.ceil(days_required)}") 
 
# # Советы по результатам подсчета 
# if days_required > 30: 
#     print( 
#         "Тестирование займет более одного месяца. Рассмотрите возможность увеличения трафика или пересмотра параметров теста.") 
# else: 
#     print( 
#         "Тестирование можно провести в течение одного месяца. Убедитесь, что у вас есть достаточные ресурсы и планирование для его проведения.")




# a = int(input())
# b = int(input())

# max_sum = 0
# max_number = 0

# for number in range(a, b + 1):
#     divisor_sum = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divisor_sum += i
#     if divisor_sum >= max_sum:
#         max_sum = divisor_sum
#         max_number = number

# print(max_number, max_sum)


# n = int(input())

# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print('+', end='')
#     print() 


# n = int(input())

# for i in range(1, n + 1):
#     # Печать чисел от 1 до i
#     for j in range(1, i + 1):
#         print(j, end="")
#     # Печать чисел от i-1 до 1
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()


# n = int(input())
# f = 1
# r = 0
# for i in range(1, n + 1):
#     f *= i
#     r += f
# print(r)    



a = int(input())
b = int(input())
div = 0
for i in range(a, b + 1):
    div = 0
    for j in range(1, i + 1):
        if i % 1 == 0 and i % j == 0:
            div += 1
    if div ==2:
        print(i)   
