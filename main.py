import math
def quadrat():
    
    a = int(input('Enter the number a: '))
    b = int(input('Enter the number b: '))
    c = int(input('Enter the number c: '))
    D = b ** 2 - 4 * a * c #search disriminant

    if D < 0:
        print('D =', D, 'There are no roots' )
    elif D == 0:
        x = -b / (2*a)
        return x
         
    else:
        print('D =', D )
        x1 = -b + math.sqrt(D) / (2*a)
        x2 = -b - math.sqrt(D) / (2*a)
        print('x1 =', x1)
        print('x2 =',  x2)
        return x1, x2
    
  
def quadrat1():
    print('Can I help you?' )
    next = input(' Enter "Yes" or "No":   '  )
    for i in next: 
        if next == 'Yes':
         quadrat()
         return quadrat1()
        elif next == 'No':
            print('Goodbye)')
            break
        
quadrat1()
    
    


    





    
    





