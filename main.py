def quadratic_solver(a, b, c):
    discriminant = b**2 - 4 * a * c
    discr_pow = pow(discriminant,(1/2))
    x1 = (-b-discr_pow)/(2*a)
    x2 = (-b+discr_pow)/(2*a)
    return [x1, x2]

# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
