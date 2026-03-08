import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f'Two real solutions, {x1} and {x2}')

elif D == 0:
    x = -b / (2*a)
    print(f'One real solution {x} for the equation')

else:
    print(f'No real solutions (discriminant {D}< 0)' )



