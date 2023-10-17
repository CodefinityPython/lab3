

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0 :
        x1 = (-b + 2 ** 1/2) / (2*a)
        x2 = (-b - 2 **1/2) / (2 * a)
        print('корені дорівнюють')
        return x1 , x2
    elif  discriminant == 0 :
        x = -b / 2 * a
        return x
    else:
        return 'коренів немає'







 # Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
