# Week 07 Lab - Data Abstraction and Magic Methods
from abc import ABC, abstractmethod

# ========================
# I. DATA ABSTRACTION
# ========================

# 1. Airplane Ticket Booking System
print("AIRPLANE TICKET BOOKING SYSTEM")
class AirplaneTicket(ABC):
    def __init__(self, passenger_name, ticket_price):
        self.passenger_name = passenger_name
        self.ticket_price = ticket_price
        self.booked = False

    def book_ticket(self):
        if not self.booked:
            self.booked = True
            print(f"🎟 Ticket booked for {self.passenger_name} - Price: ${self.ticket_price}")
        else:
            print(f"🎟 Ticket for {self.passenger_name} is already booked.")

    @abstractmethod
    def cancel_ticket(self):
        pass

    @abstractmethod
    def display_ticket_info(self):
        pass

class EconomyTicket(AirplaneTicket):
    #Economy Class 50% refund if canceled.
    
    def cancel_ticket(self):
        if self.booked:
            refund = self.ticket_price * 0.5
            print(f"❌ Ticket canceled for {self.passenger_name}. Refund Amount: ${refund}")
            self.booked = False
        else:
            print(f"No active booking for {self.passenger_name} to cancel.")
    
    def display_ticket_info(self):
        print(f"Economy Class Ticket - Passenger: {self.passenger_name}, Price: ${self.ticket_price}")


class BusinessTicket(AirplaneTicket):
    #Business Class 70% refund if canceled.
    
    def cancel_ticket(self):
        if self.booked:
            refund = self.ticket_price * 0.7
            print(f"❌ Ticket canceled for {self.passenger_name}. Refund Amount: ${refund}")
            self.booked = False
        else:
            print(f"No active booking for {self.passenger_name} to cancel.")
    
    def display_ticket_info(self):
        print(f"Business Class Ticket - Passenger: {self.passenger_name}, Price: ${self.ticket_price}")

class FirstClassTicket(AirplaneTicket):
    #First Class 90% refund if canceled.

    def cancel_ticket(self):
        if self.booked:
            refund = self.ticket_price * 0.9
            print(f"❌ Ticket canceled for {self.passenger_name}. Refund Amount: ${refund}")
            self.booked = False
        else:
            print(f"No active booking for {self.passenger_name} to cancel.")
    
    def display_ticket_info(self):
        print(f"First Class Ticket - Passenger: {self.passenger_name}, Price: ${self.ticket_price}")

#Case Study 1
print("\nCase Study 1: (Economy Ticket Booking and Cancellation)")
economy = EconomyTicket("Panha Reach", 500)
economy.book_ticket()
economy.cancel_ticket()
    
#Case Study 2
print("\nCase Study 2: (First Class Ticket Booking and Cancellation)")
first_class = FirstClassTicket("Alice Smith", 2000)
first_class.book_ticket()
first_class.cancel_ticket()

# 2. Library Management System 
class LibraryItem(ABC):
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_available = True
    
    @abstractmethod
    def borrow(self, borrower_name, user_type="student"):
        pass
    
    @abstractmethod
    def return_item(self):
        pass
    
    def display_info(self):

        status = "Available" if self.is_available else "Borrowed"
        print(f"{self.title} by {self.author} (ID: {self.item_id}) - Status: {status}")

class Book(LibraryItem):
    
    def borrow(self, borrower_name, user_type="student"):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' borrowed by {borrower_name} ({user_type}) for 14 days.")
        else:
            print(f"Book '{self.title}' is currently not available.")
    
    def return_item(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' has been returned by the borrower.")
        else:
            print(f"Book '{self.title}' was not borrowed.")


class Magazine(LibraryItem):
    
    def borrow(self, borrower_name, user_type="student"):
        if self.is_available:
            self.is_available = False
            print(f"Magazine '{self.title}' borrowed by {borrower_name} ({user_type}) for 7 days.")
        else:
            print(f"Magazine '{self.title}' is currently not available.")
    
    def return_item(self):
        if not self.is_available:
            self.is_available = True
            print(f"Magazine '{self.title}' has been returned by the borrower.")
        else:
            print(f"Magazine '{self.title}' was not borrowed.")


class ResearchPaper(LibraryItem):
    
    def borrow(self, borrower_name, user_type="student"):
        if user_type.lower() != "teacher":
            print(f"Access denied for {borrower_name}. Research Papers can only be borrowed by teachers.")
            return
        if self.is_available:
            self.is_available = False
            print(f"Research Paper '{self.title}' borrowed by teacher {borrower_name} for 30 days.")
        else:
            print(f"Research Paper '{self.title}' is currently not available.")
    
    def return_item(self):
        if not self.is_available:
            self.is_available = True
            print(f"Research Paper '{self.title}' has been returned by the teacher.")
        else:
            print(f"Research Paper '{self.title}' was not borrowed.")


print("2. LIBRARY MANAGEMENT SYSTEM")
book = Book("Introduction to Python", "Guido van Rossum", "B001")
magazine = Magazine("Tech Monthly", "Jane Smith", "M001")
research = ResearchPaper("Quantum Computing", "Dr. Alice Brown", "R001")

print("\nInitial Status:")
book.display_info()
magazine.display_info()
research.display_info()

print("\nBorrowing Examples:")
book.borrow("Reach", "student")
magazine.borrow("Reach", "student")
research.borrow("Reach", "student")          


print("\nReturning Examples:") 
book.return_item()
magazine.return_item()
research.return_item()


print("\nFinal Status:")
book.display_info()
research.display_info()
magazine.display_info()