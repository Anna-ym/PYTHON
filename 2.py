import datetime
current=datetime.datetime.now().year
final=int(input("Enter final year"))
for i in range(current,final+1):
    if i%400==0 or (i%4==0 and i%100!=0):
        print(i)