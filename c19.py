n=int(input("Enter the limit: "))
fterm=0
sterm=1
print("The series: ")
for i in range(n+1):
  lterm=fterm+sterm
  print(fterm)
  fterm=sterm
  sterm=lterm