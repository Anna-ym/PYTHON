ob=open("f1.txt","r")
ob2=open("f2.txt","w")
for line_no, line in enumerate(ob, start=1):
    if line_no % 2 != 0:  # Odd line numbers
        ob2.write(line)
ob.close()
ob2.close()
ob2=open("f2.txt","r")
content=ob2.read()
print(content)
ob2.close()
