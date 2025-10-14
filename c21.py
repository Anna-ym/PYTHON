str=input("Enter a string: ")
print("The given string is: ",str)
if str[-3: ]=='ing':
    str=str+"ly"
else:
    str=str+"ing"
print("The resultant string is: ",str)