

def quadratic_solver(a, b, c):

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:

        sqrt_discriminant = discriminant ** 0.5
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2
    elif discriminant == 0:

        x1 = -b / (2 * a)
        return x1
    else:

        return ("Немає коренів")


a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
