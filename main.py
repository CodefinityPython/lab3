
import math

def quadratic_solver(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print('x1 = %s \nx2 = %s' % (x1, x2))
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Рівняння не має дійсних коренів"

# Example usage of the function
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)