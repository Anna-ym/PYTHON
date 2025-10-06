line=list(input("Enter a line of text:").split(' '))
print(line)
wdict=dict()
for i in line:
    wdict[i]=0
for i in line:
    wdict[i]+=1
print(wdict)
