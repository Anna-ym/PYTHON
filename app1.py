class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def updatesalary(self,amount):
        self.salary+=amount
        print("Salary updated successfully!")
        print(self.salary)
    
    def displaydetails(self):
        print("ID= ",self.id)
        print("NAME= ",self.name)
        print("SALARY= ",self.salary)   

    def calculatesalary(self,monthsal):
        annual=12*monthsal
        print("Annual salary= ",annual)
        


id1=int(input("Enter your id: "))
name1=input("Enter your name: ")
salary1=int(input("Enter your salary: "))
emp1=Employee(id1,name1,salary1) 
 
id2=int(input("Enter your id: "))
name2=input("Enter your name: ")
salary2=int(input("Enter your salary: "))
emp2=Employee(id2,name2,salary2) 

print("MENU\n")
ch=0
while ch!=4: 
    print("MENU\n 1.UPDATING SALARY\n 2.DISPLAY DETAILS\n 3.CALCULATING ANNUAL SALARY\n 4.EXIT")
    ch=int(input("Enter your choice: "))    
    if ch==1:
        amount=int(input("Enter the amount to be updated: "))
        emp1.updatesalary(amount)
    elif ch==2:
        emp1.displaydetails()
    elif ch==3:
        monthsal=int(input("Enter your monthly salary: "))
        emp1.calculatesalary(monthsal)
    elif ch==4:
        print("Exiting proram...")
    else:
        print("Invalid choice ")

    