n=int(input("enter the number: "))
def fact(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        print("Enter a valid positive number ")
    else:
        return n * fact(n-1)
factorial = fact(n)
print("Factorial of ",n," = ",factorial)