# .Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Теорема Пифагора
# |AB|² = (y2 - y1)² + (x2 - x1)²
# A = √(X²+Y²) = √ ((X2-X1)²+(Y2-Y1)²)


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Пожалуйста введите число!")
    return a


def calculateSegment(a, b):
    lengthSegment = (((b[0] - a[0]) ** 2) +
                     ((b[1] - a[1]) ** 2)) ** 0.5  # формула
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(
    f"Длина отрезка: {format(calculateSegment(pointA, pointB), '.2f')}")
