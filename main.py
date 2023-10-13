

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = ( -b + math.sqrt(discriminant)) / (2*a)
        root2 = ( -b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Корені відсутні"




# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
