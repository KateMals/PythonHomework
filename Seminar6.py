# Определить является ли слово полиндромом при помощи рекурсии

# string1 = input()
# def Pallindrom(string1):
#     if len(string1) == 0 or len(string1) == 1:
#         return True
#     if string1[0] == string1[-1]:
#         return Pallindrom(string1[1:-1])
#     else:
#         return False
    
# print(Pallindrom(string1))

# Даны два массива чисел. Требуется вывести те элементы первого массива 
#(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива

# len1 = int(input("Введите кол-во элементов 1-го массива: "))
# len2 = int(input("Введите кол-во элементов 2-го массива: "))
# array1 = [int(input(f'Введите {i} элемент 1-го массива: ')) for i in range(len1)]
# array2 = [int(input(f'Введите {i} элемент 2-го массива: ')) for i in range(len2)]
# print(array1)
# print(array2)

# for i in range(len1):
#     if array1[i] not in array2:
#         print(array1[i], end = ' ')


# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит 
# количество элементов, у которых два соседних и, при этом, 
# оба соседних элемента меньше данного. Сначала вводится число N — коли-во элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# len = int(input("Введите кол-во элементов массива: "))
# array = [int(input(f'Введите {i} элемент массива: ')) for i in range(len)]
# print(array)

# count = 0
# for i in range(1, len - 1):
#     if array[i] > array[i - 1] and array[i] > array[i + 1]:
#         count += 1

# print(count)

#Распечатать список:

# list1 = [i for i in range(10)]
# print(list1) 

# Задача про зараженные холодильники

# n = int(input("Введите количество холодильников: "))
# key_virus = 'anton'
# result = []
# frage_word = ''
# for i in range(n):
#     frage = input ('Введите строку холодильника {i}')
#     for j in key_virus:
#         if j not in frage:
#             frage_word


def fridge(name):
    nik = "anton"
    index = 0
    for i in name:
        if i == nik[index]:
            index += 1
    if index == len(nik):
        return True
    return False

n = int(input("Input the number of fridges - "))
refridge = []
for j in range(n):
    refridge_name = input("Input the name - ")
if fridge(refridge_name):
    refridge.append(j + 1)
print(refridge)
