import csv
f=open("f3.csv","r")
data=csv.reader(f)
for i in data:
    print(i)
f.close()
