# print('Мы изучаем язык Python')
# print('Скоро я', 'буду программировать', 'на языке', 'Python!')
# print('1, 2, 4, 8, 16')
# print('Я', 'также', 'люблю', 'математику', '!')
# print('Я' 'люблю' 'Python' '!')
# print ('Оппенгеймер vs Барби')
# print('Здравствуй, мир!')
# print('4', '8', '15', '16', '23', '42')

# print('4')
# print('8')
# print('15')
# print('16')
# print('23')
# print('42')


# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')
# print('******')
# print('*******')

# print('Как тебя зовут?')  # вывод текста

# name = input()  # ввод текста и запись в переменную

# print('Привет,', name)  # вывод текста


# print('Как тебя зовут?')
# name = input()
# print('Привет,', name)

# print('What is your name?')
# name = input()
# print('How old are you?')
# age = input()
# print('My name is', name, 'and i am', age, 'year old.')

# team = input()
# print(team, '- чемпион!')

# str_1 = input()
# str_2 = input()
# str_3 = input()
# print(str_3)
# print(str_2)
# print(str_1)


# print('31', '12', '2019', sep='-')

# print('I', 'like', 'Python', sep='***')


# name = input()
# print('Привет,', name, end = '!')

# sep_1 = input()
# str_1 = input()
# str_2 = input()
# str_3 = input()
# print(str_1, str_2, str_3, sep = sep_1)

# # print('Java')
# # print('Ruby')
# # print('Scala')
# print('Python', end='+')  # print('C++')
# # print('GO')
# print('C#', end='=')  # print('C')
# print('awesome')
# # finish

# num = int(input())
# print(num)
# print(num + 1)
# print(num + 2)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(num1 + num2 + num3)

# num = int(input())
# v = num * num * num
# print('Объем =', v)
# s = 6 * num * num
# print('Площадь полной поверхности =', s)


# a = int(input())
# b = int(input())
# print(3*(a + b)*(a + b)*(a + b) + 275*b*b - 127*a - 41)

# a = int(input())
# print('Следующее за числом', a, 'число:', a + 1)
# print('Для числа', a, 'предыдущее число:', a - 1)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(3*(a+b+c+d))

# a = int(input())
# b = int(input())
# print(a, '+', b, '=', a+b)
# print(a, '-', b, '=', a-b)
# print(a, '*', b, '=', a*b)

# a = int(input())
# d = int(input())
# n = int(input())
# print(a * d ** (n - 1))

# a = int(input())
# print(a, 2 * a, 3 * a, 4 * a, 5 *a, sep='--')

# a = 82 // 3 ** 2 % 7
# print(a)

# a = int(input())
# b = a // 100
# print(b)

# n = int(input())
# k = int(input())
# print(k // n)
# print(k % n)

# a = int(input())
# print(a // 2 + a % 2)

# a = int(input())
# print(a // -4 * -1)

# a = int(input())
# print(a, 'мин - это', a // 60, 'час', a % 60, 'минут.')

# num = 754
# # просто берем последнюю цифру числа через % 10
# a = num % 10
# # сначала откидываем последнюю цифру числа через // 10 и получаем число 75
# # далее берем последнюю цифру у числа 75 через % 10
# b = num // 10 % 10
# # просто откидываем две последние цифры у числа через // 100
# c = num // 100
# print(a)
# print(b)
# print(c)

# print((num // 10 ** (n - i)) % 10)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100

# print(digit1, digit2, digit3, sep=',')

# Я пользуюсь подобной памяткой.

# num%10-последняя цифра.

# (num%100)//10=средняя цифра (в трёхзначном числе).

# num//100=первая цифра.

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print('Сумма цифр =', digit1 + digit2 + digit3)
# print('Произведение цифр =', digit1 * digit2 * digit3)

# num = int(input())
# digit_3 = num % 10
# digit_2 = (num // 10) % 10
# digit_1 = num // 100
# print(digit_1 * 100 + digit_2 * 10 + digit_3)
# print(digit_1 * 100 + digit_3 * 10 + digit_2)
# print(digit_2 * 100 + digit_1 * 10 + digit_3)
# print(digit_2 * 100 + digit_3 * 10 + digit_1)
# print(digit_3 * 100 + digit_1 * 10 + digit_2)
# print(digit_3 * 100 + digit_2 * 10 + digit_1)

# num = int(input())
# digit_4 = num % 10
# digit_3 = (num // 10) % 10
# digit_2 = (num // 100) % 10
# digit_1 = num // 1000
# print('Цифра в позиции тысяч равна', digit_1)
# print('Цифра в позиции сотен равна', digit_2)
# print('Цифра в позиции десятков равна', digit_3)
# print('Цифра в позиции единиц равна', digit_4)

# num = int(input())
# digit_5 = num % 10
# digit_4 = num % 100 // 10
# digit_3 = num % 1000 // 100
# digit_2 = num % 10000 // 1000
# digit_1 = num // 10000
# print(digit_1, digit_2, digit_3, digit_4, digit_5)

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a, b)

# print('*****************')
# print('*               *')
# print('*               *')
# print('*****************')

# a = int(input())
# b = int(input())
# print('Квадрат суммы', a, 'и', b, 'равен', (a + b) * (a + b))
# print('Сумма квадратов', a, 'и', b, 'равна', a * a + b * b)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a ** b + c ** d)

# a = int(input())
# print(a + a +(a * 10) + a * 100 + a +(a * 10))

# num1 = int(input())
# num2 = int(input())

# if num1 < num2:
#     print(num1, 'меньше чем', num2)
# if num1 > num2:
#     print(num1, 'больше чем', num2)

# if num1 == num2:  # используем двойное равенство
#     print(num1, 'равно', num2)
# if num1 != num2:
#     print(num1, 'не равно', num2)

# age = int(input())
# if 3 <= age <= 6:
#     print('Вы ребёнок')

# a = int(input())
# b = int(input())
# c = int(input())
# # if a == b == c:
# #     print('числа равны')
# # else:
# #     print('числа не равны')

# if a != b != c:
#     print('числа не равны')
# else:
#     print('числа равны')

# word = input()

# if word == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# num = int(input())
# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа
# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')

# num1, num2, num3 = int(input()), int(input()), int(input())

# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1

# print(counter)

# word = input()
# word_1 = input()
# if word == word_1:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# a = int(input())
# if a % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# a = int(input())
# a_1 = a // 1000
# a_2 = a // 100 % 10
# a_3 = a // 10 % 100 % 10
# a_4 = a % 1000 % 100 % 10
# if a_1 + a_4 == a_2 - a_3:
#     print('ДА')
# else:
#     print('НЕТ')

# a = int(input())
# if a >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# a = int(input())
# b = int(input())
# c = int(input())
# if c == b + b - a:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# else:
#     print(b)    


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a > b:
#     a = b
# if a > c:
#     a = c
# if a > d:
#     a = d 
# print(a)        

# age = int(input())
# if age <= 13:
#     print('детство')
# if  14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if  age >= 60:
#     print('старость')           


# a = int(input())
# b = int(input())
# c = int(input())
# sum = 0
# if a > 0:
#     sum += a
# if b > 0:
#     sum += b
# if c > 0:
#     sum += c
# print(sum)


# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)


# a = int(input())
# if a > -1 and a < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")



# a = int(input())
# if a <= -3 or a >= 7:
#         print('Принадлежит')
# else:
#     print('Не принадлежит')


# a = int(input())
# if -30 < a <= -2 or 25 >= a > 7:
#         print('Принадлежит')
# else:
#     print('Не принадлежит')


# a = int(input())
# if (a % 7 == 0 or a % 17 == 0) and (1000 <= a <= 9999):
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# b = int(input())
# c = int(input())
# if (((a + b) > c) and ((a + c) > b) and ((c + b) > a)) and (a > 0 and b > 0 and c > 0):
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a == c or b == d:
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# x = c - a
# y = d - b
# if  -1 <= x <= 1 and -1 <= y <= 1:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# k = int(input())
# if n > k:
#     print('NO')
# elif n < k:
#     print('YES')
# elif n == k:
#     print("Don't know")  


# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# elif a != b and b != c and a != c:
#     print('Разносторонний')


# a = int(input())
# b = int(input())
# c = int(input())
# if a < b < c or c < b < a:
#     print(b)
# elif c < a < b or b < a < c:
#     print(a)   
# else:
#     print(c)


# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print(31)
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print(30)
# else:
#     print(28)


# a = int(input())
# if a < 60:
#     print('Легкий вес')
# elif a < 64:
#     print('Первый полусредний вес')  
# elif a < 69:
#     print('Полусредний вес')


# a = int(input())
# b = int(input())
# c = input()
# if b == 0 and c == '/':
#     print('На ноль делить нельзя!')
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/' and c != 0:
#     print(a / b) 
# else:
#     print('Неверная операция')


# a = input()
# b = input()
# if a == b == 'красный':
#     print('красный')
# elif a == b == 'синий':
#     print('синий')
# elif a == b == 'желтый':
#     print('желтый')
# elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
#     print('фиолетовый')
# elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
#     print('оранжевый')
# elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
#     print('зеленый')
# elif a == b == 'красный':
#     print('красный')
# elif a == b == 'синий':
#     print('синий')
# elif a == b == 'желтый':
#     print('желтый')         
# else:
#     print('ошибка цвета')


# a = int(input())
# if a == 0:
#     print('зеленый')
# elif 1 <= a <= 10 and a % 2 == 0:
#     print('черный')
# elif 1 <= a <= 10 and a % 2 != 0:
#     print('красный')
# elif 11 <= a <= 18 and a % 2 == 0:
#     print('красный')
# elif 11 <= a <= 18 and a % 2 != 0:
#     print('черный')
# elif 19 <= a <= 28 and a % 2 == 0:
#     print('черный')
# elif 19 <= a <= 28 and a % 2 != 0:
#     print('красный')
# elif 29 <= a <= 36 and a % 2 == 0:
#     print('красный')
# elif 29 <= a <= 36 and a % 2 != 0:
#     print('черный')
# else:
#     print('ошибка ввода')  


# a_1 = int(input())
# b_1 = int(input())
# a_2 = int(input())
# b_2 = int(input())
# if ((a_1 < b_1) and (a_2 < b_2)) and (b_1 < a_2):
#     print('пустое множество')
# elif ((a_1 < b_1) and (a_2 < b_2)) and ((a_2 < a_1) and (b_2 < b_1)):
#     print('пустое множество')
# elif ((a_1 < b_1) and (a_2 < b_2)) and (b_1 == a_2):
#     print(b_1)
# elif ((a_1 < b_1) and (a_2 < b_2)) and (a_2 < b_1 < b_2):
#     print(a_2, b_1)
# elif ((a_1 < b_1) and (a_2 < b_2)) and ((b_2 <= b_1) and (a_1 < a_2)):
#     print(a_2, b_2)
# elif ((a_1 < b_1) and (a_2 < b_2)) and ((b_2 <= b_1) and (a_1 >= a_2)):
#     print(a_1, b_1)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
elif a1 >= a2 and b1 <= b2:
    print(a1, b1)
elif a1 <= a2 and b1 >= b2:
    print(a2, b2)
elif ((a1 < b1) and (a2 < b2)) and (b1 == a2):
    print(b1)
elif ((a1 < b1) and (b1 > a2)) and (b2 == a1):
    print(a1)         
elif a1 <= a2 and b1 <= b2:
    print(a2, b1)
elif a1 >= a2 and b1 >= b2:
    print(a1, b2)