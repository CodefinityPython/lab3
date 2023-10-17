import math


def find_quadratic_roots(a, b, c):
    # Обчислюємо дискримінант
    discriminant = b ** 2 - 4 * a * c

    # Якщо дискримінант менше 0, немає реальних коренів
    if discriminant < 0:
        return "Немає реальних коренів"

    # Якщо дискримінант дорівнює 0, є один корінь
    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    # Якщо дискримінант більше 0, є два корені
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


# Приклад використання функції
a = 2
b = -3
c = 1

roots = find_quadratic_roots(a, b, c)
print(roots)