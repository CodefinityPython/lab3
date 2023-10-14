def quadratic_solver(a, b, c):
    if(a == 0 & b == 0 & c == 0):
        return 'ZeroDivisionError: division by zero'

    # Вычисление дискриминанта
    discriminant = b**2 - 4*a*c

    # Проверка значения дискриминанта
    if discriminant > 0:
        x1 = (-b - discriminant**0.5) / (2*a)
        x2 = (-b + discriminant**0.5) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        real_part = -b / (2*a)
        imaginary_part = (abs(discriminant)**0.5) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

# Пример использования функции
a = 1
b = -4
c = 3
result = quadratic_solver(a, b, c)
print(result)