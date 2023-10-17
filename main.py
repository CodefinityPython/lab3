import math

def quadratic_solver(a, b, c):
    disc = b**2-4*a*c
    if disc > 0:
        x1 = round((-b + math.sqrt(disc)) / (2 * a), 1)
        x2 = round((-b - math.sqrt(disc)) / (2 * a), 1)
        return f"Found two equation roots: {x1}, {x2}."
    elif disc == 0:
        x = round((-b) / (2 * a), 1)
        return f"Found one equation root: {x}."
    else:
        return "No equation roots."
    

# Приклад використання функції
a = -1
b = 4
c = 3
result = quadratic_solver(a, b, c)
print(result)
