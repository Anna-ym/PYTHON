n=int(input("enter the number: "))
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
factorial = fact(n)
print("Factorial of ",n," = ",factorial)