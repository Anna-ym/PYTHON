year=int(input("Enter the year"))
print(year)
if year%400==0 or (year%4==0 and year%100!=0):
        print("The entered year is a leap year")
else:
        print("The entered year is not a leap year")
        