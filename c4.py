#program to perform arithmetic operations
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))

print("MENU\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.MODULUS\n")
ch=int(input("Enter your choice: "))
if ch==1:
    print(f"{x}+{y}={x+y}")
elif ch==2:
    print(f"{x}-{y}={x-y}")
elif ch==3:
    print(f"{x}*{y}={x*y}")
elif ch==4:
    print(f"{x}/{y}={x/y}")
elif ch==5:
    print(f"{x}%{y}={x%y}")
else:
    print("Invalid choice")