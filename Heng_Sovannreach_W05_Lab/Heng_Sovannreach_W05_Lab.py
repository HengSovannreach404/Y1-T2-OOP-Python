# I. Encapsulation
print("I. Encapsulation")
print("1. Secure Bank Account\n")

class BankAccount:
    owner = ""
    balance = 0

    def __init__(self, Owner, Balance):
        self.owner = Owner
        self.balance = Balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Attempted to withdraw $",amount)
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    def get_balance(self):
        print(f"Final Balance: ${self.balance}")

print("Case Study 1:\n")
owner1 = BankAccount("John", 1000)
owner1.deposit(500)
owner1.withdraw(200)
owner1.get_balance()

print("\nCase Study 2:\n")
owner2 = BankAccount("Reach" , 3000)
owner2.deposit(2000)
owner2.withdraw(4000)
owner2.withdraw(2000)
owner2.get_balance()


# II. Inheritance
# 3. Vehicle Management System 
print("II. Inheritance")
print("3. Vehicle Management System \n")
class Vehicle :
        def __init__(self,brand,speed):
                self.brand = brand
                self.speed = speed

        def show_info(self):
                print(f"Brand: {self.brand} , Speed : {self.speed} Km/hour",end="")

class Car(Vehicle) :
        def __init__(self,brand,speed,num_doors):
                super().__init__(brand,speed)
                self.num_doors = num_doors

        def show_info(self):
                print("Car -> ", end="")
                super().show_info()
                print(f", Doors : {self.num_doors}")

class Motorcycle(Vehicle) :
        def __init__(self,brand,speed,type_of_motorcycle):
                super().__init__(brand,speed)
                self.type_of_motorcycle = type_of_motorcycle

        def show_info(self):
                print("Motorcycle -> ",end="")
                super().show_info()
                print(f", Type : {self.type_of_motorcycle}")

class Bike(Vehicle):
        def __init__(self, brand, speed, type_of_bike):
                super().__init__(brand, speed)
                self.type_of_bike = type_of_bike

        def show_info(self):
                print("Bike -> ",end="")
                super().show_info()
                print(f", Type: {self.type_of_bike}")

# Case 1
print("Case Study 1:")
car1 = Car("Volvo", 120, 4)
car1.show_info()
motorcycle1 = Motorcycle("Harley-Davidson", 150, "Cruiser")
motorcycle1.show_info()
bike1 = Bike("Trek", 25, "Mountain")
bike1.show_info()

# Case 2
print("Case Study 2:")
car2 = Car("Lamborghini", 300, 2)
car2.show_info()
motorcycle2 = Motorcycle("Ducati", 200, "Sport")
motorcycle2.show_info()
bike2 = Bike("Giant", 40, "Road")
bike2.show_info()
print("\n\n")

# III. Polymorphism 
# Exercise 4
print("II. Inheritance")
print("4. Employee Salary Calculation \n")
class Employee :
        def __init__(self,name,base_salary):
                self.name = name
                self.base_salary = base_salary

        def calculate_salary(self):
                return  self.base_salary

class Manager(Employee):
        def __init__(self,name,base_salary):
                super().__init__(name,base_salary)

        def calculate_salary(self):
                return self.base_salary + 2000

class Developer(Employee):
        def __init__(self,name,base_salary):
                super().__init__(name,base_salary)

        def calculate_salary(self):
                return  self.base_salary * 1.10

class Intern(Employee):
        def __init__(self,name,base_salary):
                super().__init__(name,base_salary)

        def calculate_salary(self):
                return 1500

# case 1
print("Case Study 1:")
manager1 = Manager("Sophia", 6000)
print(f"👩 Manager: {manager1.name}'s Salary: ${manager1.calculate_salary():,.2f}")
developer1 = Developer("Jake", 4000)
print(f"👨 Developer: {developer1.name}'s Salary: ${developer1.calculate_salary():,.2f}")
intern1 = Intern("Liam", 0)
print(f"🧑 Intern: {intern1.name}'s Salary: ${intern1.calculate_salary():,.2f}")

# case 2
print("Case Study 2:")
manager2 = Manager("Alex", 10000)
print(f"👩 Manager: {manager2.name}'s Salary: ${manager2.calculate_salary():,.2f}")
developer2 = Developer("Mia", 7000)
print(f"👨 Developer: {developer2.name}'s Salary: ${developer2.calculate_salary():,.2f}")
intern2 = Intern("Emma", 0)
print(f"🧑 Intern: {intern2.name}'s Salary: ${intern2.calculate_salary():,.2f}")


# IV. Mixed Concepts
# 5. Handling Different Types of Data 
print("IV. Mixed Concepts")
print("5. Handling Different Types of Data \n")
class Data:
        def __init__(self):
                self.__data = None

        def process_data(self):
                pass

class NumericalData(Data):
        def __init__(self,numbers):
                super().__init__()
                self.__numbers = numbers

        def process_data(self):
                if self.__numbers:
                        sum(self.__numbers) / len(self.__numbers)
                        return sum(self.__numbers) / len(self.__numbers)
                return 0

class TextData(Data):
        def __init__(self,text):
                super().__init__()
                self.__text = text

        def process_data(self):
                words = self.__text.split()
                return len(words)

class CategoricalData(Data):
         def __init__(self,categories):
                 super().__init__()
                 self.__categories = categories

         def process_data(self, category=None):
                 if category:
                         return self.__categories.count(category)
                 return 0


# case 1
print("\n===== Case Study 1: Numerical Data =====")
num_data = NumericalData([10, 20, 30, 40, 50])
print(f"Mean of all numbers: {num_data.process_data()}")

print("\n===== Case Study 2: Text Data =====")
text_data = TextData("Data science is fun and easy to learn")
print(f"Number of words: {text_data.process_data()}")

print("\n===== Case Study 3: Categorical Data =====")
cat_data = CategoricalData(["cat", "dog", "dog", "cat", "bird", "cat"])
print(f"Frequency of 'dog': {cat_data.process_data('dog')}")