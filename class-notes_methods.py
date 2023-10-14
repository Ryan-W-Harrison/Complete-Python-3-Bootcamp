
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


        