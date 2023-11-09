

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + 2 ** 1/2) / (2*a)
        root2 = (-b - 2 **1/2) / (2*a)
        print("Корені =")
        return root1, root2
    elif  discriminant == 0 :
        a = -b / (2*a)
        return a
    else:
        return "Корені відсутні"




# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
