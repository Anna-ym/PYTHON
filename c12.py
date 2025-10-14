colors=input("enter a list of colours: ").split(',')
list=[]
for i in colors:
    list.append(i)
l1=list[0]
l2=list[-1]
print("first color= ",l1 ,"last color= ",l2)