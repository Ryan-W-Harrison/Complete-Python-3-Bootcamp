
mylist = [1, 2, 3]
myset = set()
type(myset)

class Sample():
    pass

my_sample = Sample()
type(my_sample)

class Dog():
    # Class object attribute
    # Same for any instance of a class
    species = "mammal"

    def __init__(self, breed, name, spots):
        # Attributes
        # We tak in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect a boolean
        self.spots = spots
    
    # Operations/Actions --> Methods
    def bark(self, number):
        #print("WOOF! My name is {}".format(self.name))
        print(f'WOOF! My name is {self.name} and the number is {number}')

type(my_dog)
my_dog.breed
my_dog = Dog(breed = 'lab', name = 'Sammy', spots = False)
my_dog.bark(number = 3)

#----------------

class Circle():
    # CLass object attribute
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi
    
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle()
my_circle.get_circumference()
my_circle.area

class Animal():
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

myanimal = Animal()
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

mydog = Dog()

mydog.who_am_i()

# Special Methods
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")
        

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book

# OOP Homework
# Problem 1: Line class
# Given 2 sets of coordinates in a tuple,
# calculate the distance and calculate the slope between 2 points
# d = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# slope = (y2 - y1) / (x2 - x1)


class Line:
    import math
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    
    def distance(self):
        return math.sqrt( (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 )
    
    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()

# Problem 2:

class Cylinder:
    import math
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return math.pi * self.height * (self.radius)**2
    
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius)**2)
    
# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()

c.surface_area()

# OOP Challenge
# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:
# 
# * owner
# * balance
# 
# and two methods:
# 
# * deposit
# * withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'
    
    def deposit(self, amount):
        print("Deposit Accepted")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            print("Withdrawal Accepted")
            self.balance -= amount
            return self.balance
        else:
            print("Funds Unavailable!")
            return self.balance
        
acct1 = Account('Jose', 100)
print(acct1)
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

# Modules and packages
import requests

# export PATH=”$PATH:/usr/local/bin/python
# /usr/bin/python3.10
# 
# echo export PATH="/usr/bin/python3.10:$PATH" >> ~/.profile


from colorama import init
init()
from colorama import Fore
print(Fore.RED + "some red text")
print(Fore.GREEN + "switch to green")

import openpyxl

# Modules are just .py scripts
# Packages are collections of modules, but requires the __init__.py script
# Check out the files "mymodule.py", "myprogram.py", "MyMainPackage/"

# __name__ and __main__
if __name__=="__main__"

# Exceptions and error handling

def add(n1, n2):
    print(n1+n2)
    
add(10, 20)

number1 = 10
number2 = input("Please provide a number: ")

add(number1, number2)

try:
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("ther was a type error!")
except OSError:
    print('Hey you have an OS error!')
except SyntaxError:
    print("Syntax error")
finally:
    print("I always run")
    

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")
            
ask_for_int()


# Errors and Exceptions Homework

# Problem 1
# Handle the exception thrown by the code below by using try and except blocks

for i in ['a', 'b', 'c']:
    print(i**2)
    
# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done'
# x=5
# y=0
# z = x/y

x = 5
y = 0
try:
    z = x / y
except:
    print("Divide by zero error!")
finally:
    "All Done"
    

# Problem3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs
def ask():
    pass

ask()
