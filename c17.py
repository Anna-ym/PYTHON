l=map(int,input("enter a list of numbers: ").split(','))
list=[]
list1=[]
for i in l:
    list.append(i)
print(list)
for j in list:
    if j%2!=0:
        list1.append(j)
print("The new list: ",list1)