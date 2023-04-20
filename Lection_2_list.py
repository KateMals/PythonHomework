
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

"""Удаление последнего элемента"""

# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop()
# print(list_1)

"""Удаление конкретного элемента"""
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop(1))
# print(list_1)

"""Добавление элемента на конкретную позицию"""

# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.insert(2, 11))
# print(list_1)
#индексы: 0  1  2  3  4  5  6  7  8  9
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])
# print(list_1[1])
# print(list_1[-1]) # выводит последний элемент с конца
# print(list_1[-5]) #выводит 5й элемент с конца -"6"
# print(list_1[len(list_1)-1]) # выводит последний элемент с конца
# print(list_1[:]) #выводит весь список
# print(list_1[:2]) #выводит первые три элемента с индексами 0,1,2 но послед.не берется
# print(list_1[len(list_1)-2:]) #выводит первые два последних элемента
# print(list_1[2:9]) #c индекса 2 по 9,но без последнего
# print(list_1[0:len(list_1):6]) #с 0го элемента с шагом 6
# print(list_1[::6]) #с 0го элемента с шагом 6
# print(list_1[::2])


#кортеж - неизменяемый список (список который нельзя менять) type - tuple
# t = ()
# print(type(t))

# t = (1, )
# print(type(t))

# t = (1, 2, 66, 78)
# print(type(t))

# v = [1, 5, 7] #список
# print(v)
# print(type(v)) # определяет тип - список
# v = tuple(v) # задаем тип кортежа этому списку
# print(type(v))
# print(v)

# a, b, c = v
# print(a)
# print(a, b, c)

t = (1, 2, 3, 4, 5)
# вывод конкретного значение по индексу:
# print(t[1])

# вывод значений списка поочередно-используем цикл
# for i in t:
#     print(i)

# вывод значений списка поочередно-используем цикл
# for i in range(len(t)):
#     print(t[i])


# в кортеже значения изменить нельзя, чтобы изменить значение нужен формат списка:
"""
t = [1,2,3,4]
print(t)
t[1] = 333
print(t[1])
print(t)
"""

#Словари-неупорядоченные коллекции произвольных объектов с доступом по ключу
# Ключ - срока,число

# d = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])


# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'right': '→', 'down': '↓'}
# print(dictionary)
# # print(dictionary['left'])
# # del dictionary['left']  #удаление конкретного элемента из словаря
# # print(dictionary)
# for item in dictionary:
#     print(item)
#     print('{}:{}'.format(item, dictionary[item])) 

# выводит ключи и значения:
# print(dictionary.items())
# for (k,v) in dictionary.items():
#     print(k,v)


# Множества содержат в себе уникальные элементы {}

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('gray') # добавить значение
# print(colors)
# colors.remove('red')  # удалить значение
# colors.discard('red') # проверяет есть ли это значение в множестве для дальнейшего удаления
# print(colors)

# colors.clear() #удалить все значения
# print(colors)

# q = set() #создать множество "set()"


# Операции со множествами

# a = {1, 2, 3, 6, 7}
# b = {6, 7, 8, 9, 10}
# print(a)
# print(b)
# c = a.copy() #скопировать множество в "с"
# print(c)

# u = a.union(b) # объединяет уникальные значения из 2х множеств a и b 
# print(u)

# i = a.intersection(b) #находит пересечение (одинак.объекты)
# print(i)

# d1 = a.difference(b)
# print(d1)

# d2 = b.difference(a)
# print(d2)

# q = a.union(b).difference(a.intersection(b))
# print(q)


a = {1, 8, 6}
b = frozenset(a) #заморозить множество и перенести в новую переменную
print(b)