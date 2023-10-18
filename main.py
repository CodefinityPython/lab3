import math

def quadratic_solver(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return f'x1 = {x1}, x2 = {x2}'
    elif disc == 0:
        x = -b / (2 * a)
        return f'рівняння має один корінь, x = {x}'
    else:
        return "коренів немає"

    


# Приклад використання функції
a = 1
b = -2
c = 1
result = quadratic_solver(a, b, c)
print(result)
