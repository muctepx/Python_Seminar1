#Задача 3
#""" Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
#Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3  """

from os import system
system("cls")
print ("Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, \n в которой находится эта точка (или на какой оси она находится).")
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка находится в 1й четверти")
elif x < 0 and y > 0:
    print("Точка находится в 2й четверти")
elif x < 0 and y < 0:
    print("Точка находится в 3й четверти")
elif x > 0 and y < 0:
    print("Точка находится в 4й четверти")
elif x == 0 and y == 0:
    print("Точка находится центре оси координат")
elif x == 0:
    print("Точка находится на оси х")
elif y == 0:
    print("Точка находится на оси y")