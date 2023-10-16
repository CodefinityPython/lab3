

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2*a)
        root2 = (-b - discriminant ** 0.5) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root)
    else: 
        return None




# Приклад використання функції
a = 1
b = 3
c = 7
result = quadratic_solver(a, b, c)


if result: 
    print(f"Корені рівняння: {result}")
else:
    print("Немає дійсних коренів в рівнянні")
