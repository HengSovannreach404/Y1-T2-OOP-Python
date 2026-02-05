# Exercise 01
print("Exercise 1")


class Car:
    Make = ""
    Model = ""
    Year = 0

    def __init__(self, make, model, year):
        self.Make = make
        self.Model = model
        self.Year = year

    def display_info(self):
        print("Car details:")
        print("Make: ", self.Make)
        print("Model: ", self.Model)
        print("Year: ", self.Year)

car0 = Car("Toyota", "Corolla", 2020)
car0.display_info()

print()
# Exercise 02
print("Ecercise 2")


class Car2:
    Makes = ""
    Models = ""
    Years = 0

    def __init__(self, makes, models, years):
        self.Makes = makes
        self.Models = models
        self.Years = years

    def is_vintage(self):
        if 2026 - self.Years > 25:
            vintage = True
        else:
            vintage = False
        return vintage


Car1 = Car2("Toyota", "Corolla", 2020)
car2 = Car2("ferri", "f1", 1999)
print(f"Car 1 is vintage: {Car1.is_vintage()}")
print(f"Car 2 is vintage: {car2.is_vintage()}")

print()

# Exercise 03
print("Exercise 3")


class Student:
    Name = ""
    Age = 0
    grade = ""

    def __init__(self, name, age, grade):
        self.Name = name
        self.Age = age
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def student_info(self):
        print("Name: ", self.Name)
        print("Age: ", self.Age)
        print("Grade: ", self.grade)


student1 = Student("John", 20, "B")
print("Before grade update:")
student1.student_info()


student1.update_grade("A")
print("After grade update:")
student1.student_info()

print()

# Exercise 04
print("Exercise 4")


class BankAccount:
    owner = ""
    balance = 0

    def __init__(self, Owner, Balance):
        self.owner = Owner
        self.balance = Balance

    def deposit(self, amount):
        self.balance += amount
        print("Depositing $", amount)
        print("New balance: $", self.balance)

    def withdrawing(self, amount):
        if amount > self.balance:
            print("Attempting to withdraw $", amount)
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print("Withdrawing $", amount)
            print("New balance: $", self.balance)


owner1 = BankAccount("John", 1000)
print(f"Initial balance for {owner1.owner}: ${owner1.balance}")
owner1.deposit(500)
owner1.withdrawing(300)
owner1.withdrawing(2000)
print("Final balance: $", owner1.balance)

print()


# Exercise 05
print("Exercise 5")


class Book:
    title = ""
    author = ""
    price = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Library:
    books = []

    def __init__(self):
        pass

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Books in the library:")
        print()
        for i in range(len(self.books)):
            print(f"{i+1}. Title: {self.books[i].title}, Author: {self.books[i].author}, Price: ${self.books[i].price}")


book1 = Book("The Great Man", "F. Ane Fit", 10.99)
book2 = Book("The story about APT", "Fake Man", 12.50)
book3 = Book("1984", "George Orwell", 9.75)
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.show_books()

print()

# Exercise 06
print("Exercise 6")
class Classroom:
    class_name = ""
    Students =[]
    def __init__(self, class_name):
        self.class_name = class_name
    def add_student(self , name):
        self.Students.append(name)
        print("Added Student:",name)
    def list_students(self):
        print("Student in ", self.class_name,":")
        for i in range(len(self.Students)):
            print("- ",self.Students[i])


class1 = Classroom("Math 101")
class1.add_student("Alice")
class1.add_student("Bob")
class1.add_student("Charlie")
class1.list_students()

print()


# Exercise 07
print("Exercise 7")
class PhoneBook: 
    contacts = {}
    def __init__(self):
        pass

    def add_contact(self,name , number):
        self.contacts.update({name : number})
        print("Added contact: ",name ,"->" ,number)
    
    def find_contact(self , name):
        if name in self.contacts:
            print(f"{name}'s number: ", self.contacts[name])
        else:
            print(name ,"not found in phone book.")
contact = PhoneBook()
contact.add_contact("John", "123-456-7890")
contact.add_contact("Jane", "987-654-3210")
contact.find_contact("John")
contact.find_contact("Alice")

print()

#Exercise 8
print("Exercise 8")
class SportsLeague:
    teams = {}
    def add_team(self , team_name):
        if team_name not in self.teams:
            print(f"Team '{team_name}' added.")
            self.teams.update(team_name)
        else:
            print(f"Team '{team_name}' is already exited.")