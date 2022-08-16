class rectangle:
   
    def area(self):
        l=float(input("enter lenth:"))
        b=float(input("enter breadth:"))
        return l*b
class circle:
  
    def area(self):
        r=float(input("enter radious:"))
        return r*r*3.14


obj = rectangle()
obj1=circle()
choice = 1
while choice != 0:
    print("1. rectangle")
    print("2. circle")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(obj.area())
    elif choice == 2:
        print(obj1.area())