start=int(input("Enter the starting year"))
end=int(input("Enter the ending year"))
print(start,end)
for i in range(start,end+1):
    if i%400==0 or (i%4==0 and i%100!=0):
        print(i)