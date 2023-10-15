import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        result1 = (-b + math.sqrt(discriminant)) / (2*a)
        result2 = (-b - math.sqrt(discriminant)) / (2*a)
        return result1, result2
    elif discriminant == 0:
        result = -b / (2*a)
        return result
    else:
        return "No real solver"
# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
