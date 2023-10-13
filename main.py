
def quadratic_solver(a, b, c):
    # Розрахунок дискримінанту
    discriminant = b**2 - 4*a*c
    
    # Перевірка дискримінанту
    if discriminant > 0:
        # Два різних корені
        root1 = (-b + discriminant ** 0.5) / (2*a)
        root2 = (-b - discriminant ** 0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # Один дубльований корінь
        root = -b / (2*a)
        return root
    else:
        # Відсутність реальних коренів
        return "Корені відсутні"

# Приклад використання функції:
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)

