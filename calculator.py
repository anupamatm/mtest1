class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


class Usecalculator():
    
    def inp(self):
        x = int(input("enter first number:"))
        y = int(input("enter second number"))
        obj = Calculator(x, y)
        choice = 1
        while choice != 0:
            print("1. ADDITION")
            print("2. SUBTRACTION")
            print("3. MULTIPLICATION")
            print("4. DIVISION")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print(obj.add())
            elif choice == 2:
                print(obj.sub())
            elif choice == 3:
                print(obj.mul())
            elif choice == 4:
                print(obj.div())
            else:
                print("Invalid choice")


e = Usecalculator()
e.inp()
