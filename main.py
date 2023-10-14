from math import sqrt


def quadratic_solver(a, b, c):
    d = b**2 - 4 * a * c
    if (d < 0):
        return "Коренів немає."
    elif (d == 0):
        x = (-b - sqrt(d)) / 2*a
        return f"Корінь: {x}"
    else:
        x1 = (-b - sqrt(d)) / 2*a
        x2 = (-b + sqrt(d)) / 2*a
        return f"Корені: x1 = {x1}, x2 = {x2}"






# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
