x=int(input("enter first number"))
y=int(input("enter second number"))
list1=[]
list2=[]
for i in range(1,x+1):
    if x%i==0:
        list1.append(i)
for j in range(1,y+1):
    if y%j==0:
        list2.append(j)
print(list1)
print(list2)
for i in list1:
    for j in list2:
        if i==j:
            gcd=i
print("gcd= ",gcd)
        