import math

def quadratic_solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / 2 * a
        x2 = (-b + math.sqrt(discriminant)) / 2 * a
        return (x1, x2)
    elif discriminant == 0:
        x = -b / 2 * a
        return x
    else:
        return ("Коренів не має.")

# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
