"""Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
каждый символ уже встречался. Количество повторов добавляется к символам с помощью
постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split() """

# text = "a a a b c a a d c d d".split()
# res = {}
# for i in text:
#     if i not in res:
#         res[i] = 0
#         print(i, end = " ") 
#     else:
#         res[i] += 1
#         print(i, "_", res[i], end = " ")    

    

res = {}
for i in "a a a b c a a d c d d":
    if i not in res:
        res[i] = 0
        print(i, end = "") 
    else:
        res[i] += 1
        print(i,"_",res[i],end="")
       











""" Пользователь вводит текст(строка). Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea 
shore shells
Output: 13 """
"""
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text = text.upper()
text = text.split()
text = set(text)
text = str(text)
print(text)
count = text.count(" ") + 1
print(count)
"""