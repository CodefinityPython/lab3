def quadratic_solver(a, b, c):
    #шукаємо дискримінант
    discriminant = b**2 - 4 * a * c
    #якщо d < 0 то немає рішень
    if discriminant < 0:
        return 'Немає коренів!'
    #шукаємо корінь дискримінанта
    discr_pow = pow(discriminant,(1/2))
    #якщо d = 0:
    if discriminant == 0:
        return (-b-discr_pow)/(2*a)
    #якщо d > 0:
    else:
        x1 = (-b-discr_pow)/(2*a)
        x2 = (-b+discr_pow)/(2*a)
        return [x1, x2]

# Приклад використання функції
a = 1
b = -3
c = 2

result = quadratic_solver(a, b, c)
print(result)


