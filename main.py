
def quadratic_solver(a, b, c):

    D = b** 2 - 4 * a * c
    print("Discriminant = ", D)

    if D > 0:
        print("There are two real solutions:")
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif D == 0:
        print("There is one real solution:")
        x = -b / (2*a)
        print(f"x = {x}")
    else:
        print("There are no real solutions!")

# Приклад використання функції
result = quadratic_solver(2, -7, 6)
print(result)
