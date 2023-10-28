# Class Notes decorators
def func():
    return 1
  
func()

func

def hello():
    return "Hello!"
  
hello()

greet = hello # greet copies hello instead of just pointing

greet()

hello()
del hell
hello()
greet()


def hello(name = 'Jose'):
    print("The hello() function has been executed!")
    
    def greet():
        return '\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
      
    print(greet())
    print(welcome())
    print('This is the end of hello function!')
      
hello()
welcome()



def hello(name = 'Jose'):
    print("The hello() function has been executed!")
    
    def greet():
        return '\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
      
    print('I am going to return a function!!')
    if name == "Jose":
        return greet
    else:
        return welcome
      
my_new_func = hello('Jose')
my_new_func()

my_new_func2 = hello('Plumbus')
my_new_func2()

def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()
some_func
some_func()

def hello():
    return 'Hi Jose!'
  
def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

hello()
other(hello)

def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        
        print('Some extra code, after the original function!')
        
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!!")

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")

func_needs_decorator()

#@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")

func_needs_decorator()


