import csv
with open('f5.csv','w')as file:
    dict={'a':'apple','b':'bat','c':'cat'}
    dict1={'d':'dog','e':'egg'}
    print(dict)
    print(dict1)
    writer=csv.writer(file)
    for key,value in dict.items():
        writer.writerow([key,value])
    for key,value in dict1.items():
        writer.writerow([key,value])
print("Dictionaries copied to file")
file.close()
with open('f5.csv','r')as file:
    reader=csv.DictReader(file)
    print(reader)
print("File Copied")
file.close()