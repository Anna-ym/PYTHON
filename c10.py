import math
a=complex(input("Enter coefficient of x^2: "))
b=complex(input("Enter coefficient of x: "))
c=complex(input("Enter constant"))
eq=a*(x^2)+b*x+c
print(eq)
d=b^2-(4*a*c)
q1=(-b+d)/2*a
q2=(-b-d)/2*a
print("The roots of the given equations are ",q1,q2)
