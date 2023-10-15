import math

def quadratic_solver(a, b, c):

    discr = b ** 2 - 4 * a * c
    
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return (f'x1 = {x1}\nx2 = {x2}')
    elif discr == 0:
        x = -b / (2 * a)
        return (f'Рівняння має один корінь, x = {x}')
    else:
        return ("Коренів немає :(")

# Приклад використання функції
a = int(input('Введіть a: '))
b = int(input('Введіть b: '))
c = int(input('Введіть c: '))
result = quadratic_solver(a, b, c)
print(result)
