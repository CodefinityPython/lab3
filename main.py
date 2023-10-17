
import math
def quadratic_solver(a, b, c):
    d = b**2-4*a*c
    if d > 0 :
     x_1 = round(-b + math.sqrt(d)/(2*a), 1)
     x_2 = round(-b - math.sqrt(d)/(2*a), 1) 
     return(f"Roots: {x_1}:{x_2}. ")
    elif d==0:
       x = round(-b /(2*a), 1)
       return(f"Roots: {x}. ")
    else:
       return("No Root")   
# Приклад використання функції
a = 1
b = -3
c = 2
result = quadratic_solver(a, b, c)
print(result)
