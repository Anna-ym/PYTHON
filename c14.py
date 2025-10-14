dict={"d":"dog","a":"apple", "c":"cat","b":"bat"}
print(dict)

print("Keys: ",sorted(dict.keys()))
print("Values: ",sorted(dict.values()))
print(sorted(dict.items()))
                
items=list(dict.items())
n=len(items)
for i in range(n-1):
    for j in range(0,n-i-1):
        if items[j][1]>items[j+1][1]:
            items[j],items[j+1]=items[j+1],items[j]
sorted=items
print("The sorted dictionary= ", sorted)
    

