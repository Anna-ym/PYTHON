str=input("Enter a string: ")
print("The entered string is: ",str)
wdict=dict()
for i in str:
    wdict[i]=0
for i in str:
    wdict[i]+=1
print("The frequency of each characters in ",str," is: ",wdict)
