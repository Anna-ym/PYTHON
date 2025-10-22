class Time:
    def __init__(self,h=0,m=0,s=0):
        self.hr=h
        self.min=m
        self.sec=s
    
    def display(self):
        print(self.hr,":",self.min,":",self.sec)
    def set_time(self,h=0,m=0,s=0):
            self.hr=h
            self.min=m
            self.sec=s
        
    def __add__(self,other):
        h=self.hr+other.hr
        m=self.min+other.min
        s=self.sec+other.sec
        if s>=60:
            s-=60
            m+=1
        if m>=60:
            m-=60
            h+=1
        if h>=24:
            h-=24
        return Time(h,m,s)
'''hr=int(input("Enter the hour: "))
min=int(input("\nEnter the minute: "))
sec=int(input("Enter the second: "))     
t = Time(hr,min,sec)
t.display()'''

t1=Time(2,45,30)
t2=Time(1,20,45)
print("First time:")
t1.display()
print("Second time:")
t2.display()
t3=t1+t2
print("Added Time:")
t3.display()
    