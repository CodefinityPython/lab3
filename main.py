

def quadratic_solver(a, b, c):
    # Обчислюємо дискримінант
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        # Два дійсних корені
        x1 = ( -b + (discriminant)**0.5) / (2*a)
        x2 = ( -b - (discriminant)**0.5) / (2**a)
        return (x1, x2)
    elif discriminant == 0:
        # Один дійсний корніь (корені співпадають)
        x = -b / (2*a)
        return x
    else:
        # "Корені відсутні  ( корені комплексні)"
        return "Корені відсутні  ( корені комплексні)"




# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)