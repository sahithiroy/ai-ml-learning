"""
OOP practice problems with simple implementations.

1. Bank Account class
   - Create objects
   - Update attributes
   - Print details
   - Deposit/withdraw balance

2. Student class
3. Employee class
4. Car class
5. Book class

6. Animal hierarchy with method overriding and super()
7. Vehicle Management System
8. Payment Gateway System
9. Library Management System
10. Custom Vector class
11. Custom Fraction class
12. Student Management System with add/delete/search/update/save features
"""


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Example usage for BankAccount
account = BankAccount("Alice", 1000)
account.deposit(500)      # Output: balance becomes 1500
account.withdraw(200)     # Output: balance becomes 1300
account.show_details()    # Output: Account Holder: Alice, Balance: 1300


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_details(self):
        print(f"Student: {self.name}, Grade: {self.grade}")


student = Student("Bob", "A")
student.show_details()    # Output: Student: Bob, Grade: A


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")


employee = Employee("Charlie", 50000)
employee.show_details()  # Output: Employee: Charlie, Salary: 50000


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Car: {self.brand} {self.model}")


car = Car("Toyota", "Corolla")
car.show_details()       # Output: Car: Toyota Corolla


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print(f"Book: {self.title} by {self.author}")


book = Book("Python Basics", "John")
book.show_details()      # Output: Book: Python Basics by John


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")


animal = Dog("Buddy")
animal.speak()          # Output: Animal speaks / Dog barks


class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print("Vehicle is moving")


class CarVehicle(Vehicle):
    def drive(self):
        print("Car is moving")


vehicle = CarVehicle("Sedan")
vehicle.drive()          # Output: Car is moving


class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")


class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"PayPal processed {amount}")


paypal = PayPal()
paypal.process_payment(100)  # Output: PayPal processed 100


class LibraryBook:
    def __init__(self, title, available=True):
        self.title = title
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed")
        else:
            print(f"{self.title} is not available")


book_item = LibraryBook("Python Guide")
book_item.borrow()       # Output: Python Guide borrowed


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def show(self):
        print((self.x, self.y))


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
v3.show()                # Output: (4, 2)


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        from math import gcd
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def show(self):
        print(f"{self.numerator}/{self.denominator}")


fraction = Fraction(4, 8)
fraction.simplify()
fraction.show()          # Output: 1/2


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_no, name):
        self.students[roll_no] = name
        print(f"Added {name}")

    def delete_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            print(f"Deleted {roll_no}")
        else:
            print("Student not found")

    def search_student(self, roll_no):
        if roll_no in self.students:
            print(self.students[roll_no])
        else:
            print("Student not found")

    def update_student(self, roll_no, new_name):
        if roll_no in self.students:
            self.students[roll_no] = new_name
            print(f"Updated {roll_no}")
        else:
            print("Student not found")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for roll_no, name in self.students.items():
                file.write(f"{roll_no}:{name}\n")
        print(f"Saved to {filename}")


sms = StudentManagementSystem()
sms.add_student(1, "Asha")      # Output: Added Asha
sms.search_student(1)           # Output: Asha
sms.update_student(1, "Kavya")  # Output: Updated 1
sms.delete_student(1)           # Output: Deleted 1
