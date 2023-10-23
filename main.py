import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return ((-b + math.sqrt(discriminant)) / (2*a), (-b - math.sqrt(discriminant)) / (2*a))
    elif discriminant == 0:
        return -b / (2*a)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

a, b, c = 1, -3, 2
result = quadratic_solver(a, b, c)
print(result)




