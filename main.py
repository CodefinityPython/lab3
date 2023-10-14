# Function for discriminant
def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the value of the discriminant
    if discriminant > 0:
        # Two real roots
        x1 = (-b - discriminant**0.5) / (2*a)
        x2 = (-b + discriminant**0.5) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # One real root
        x = -b / (2*a)
        return x
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = (abs(discriminant)**0.5) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

# Example of using the function
a = 4
b = 1
c = 4
result = quadratic_solver(a, b, c)
print(result)