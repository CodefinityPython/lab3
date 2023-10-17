

def quadratic_solver(a, b, c):
    diskr = b ** 2 - 4 * a * c

    if diskr > 0 :

        x1 = (-b + 2 ** 1/2) / (2 * a)
        x2 = (-b - 2 ** 1/2) / (2 * a)
        print('Корені дорівнюють:')
        return x1 , x2

    elif diskr == 0 :
        x = -b / 2 * a
        return x

    else:
        return 'Коренів немає'

# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
