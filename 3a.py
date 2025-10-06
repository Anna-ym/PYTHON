lst=list(map(int,input("Enter list of numbers: ").split(',')))
print(lst)
n=[num for num in lst if num>0]
print(n)
for num in lst:
    if num>0:
        print(num)