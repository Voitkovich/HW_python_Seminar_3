
# Домашка семинар 3

# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number = (input("Введи значения через пробел: ")).split()
sum = 0
for i in range(len(number)):
    if i % 2 != 0:
        sum += int(number[i])
print(sum)


# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


lst = list(map(int, input("Введите числа через пробел:\n").split()))

new_list = []
for i in range(0, (len(lst) -1)//2+1):
    new_list.append(int(lst[i])*int(lst[len(lst)-i-1]))
print(new_list)

l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
print(new_lst)



# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# My_list = input("Введи значения через пробел: ").split()
# max = 0
# min = 1

# for i in range(len(My_list)):
#     My_list[i] = float(My_list[i])
#     if float (i) % 1 !=0:
#             if float(i) % 1 < min:
#                 min = float(i) % 1
#             if float(i) % 1 > max:
#                 max = float(i) % 1
# print(round(max-min),2)         


My_list = input("Введи значения через пробел: ").split()
max = 0
min = 1

for i in My_list:
    if float (i) % 1 !=0:
            if float(i) % 1 < min:
                min = float(i) % 1
            if float(i) % 1 > max:
                max = float(i) % 1
print(str(max-min)[:4])    
     


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input('Введите число: '))
My_num = ''
while num > 0:
    My_num = str(num % 2)+My_num
    num //= 2

print(My_num)    