import cmath as m
a=complex(input("Enter coefficient of x^2: "))
b=complex(input("Enter coefficient of x: "))
c=complex(input("Enter constant"))
d=b*b-(4*a*c)
x=m.sqrt(d)
q1=(-b+x)/2*a
q2=(-b-x)/2*a
print("The roots of the given equations are ",q1,q2)
