def quadratic_solver(a, b, c):
    
    discriminator = b**2 - 4*a*c
    
    if discriminator > 0:
        root1 = (-b + discriminator**0.5) / (2*a)
        root2 = (-b - discriminator**0.5) / (2*a)
        return root1, root2
    elif discriminator == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No roots"

# Приклад використання функції
a = 3
b = -1
c = 1
result = quadratic_solver(a, b, c)
print(result)