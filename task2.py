#Задача 2
#""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """

from os import system
system("cls")
print ("Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.")
x1 = [True, False]
y1 = [True, False]
z1 = [True, False]
for x in x1:
    for y in y1:
        for z in z1:
            print(x, y, z)
            res1 = not (x or y or z)
            res2 = (not x) and (not y) and (not z)
            print(res1 == res2)