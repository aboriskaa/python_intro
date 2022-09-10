# Task 1
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.

a = int(input('Номер дня недели:'))
if (a > 5):
    print('Это выходной день')
elif (a > 7):
    print('Нет такого дня недели')
else:
    print('Это рабочий день')

# Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result
