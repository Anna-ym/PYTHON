dict1={"a":"apple","b":"bat","c":"cat"}
dict2={"d":"dog","e":"elephant"}
print(dict1)
print(dict2)
merge_dict={}
for d in (dict1,dict2):
    for key,value in d.items():
        merge_dict[key]=value
print("after merging: ",merge_dict)
dict={}
k=input("Enter keys for dictionary: ")
v=input("Enter values for dictionary: ")
for i in (k,v):
    dict[k]=v
print(dict)
    
