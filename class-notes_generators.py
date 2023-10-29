# class Notes generators

def create_cubes(n):
    for x in range(n):
        yield(x**3)
        
for x in create_cubes(10):
    print(x)

create_cubes(10)

list(create_cubes(10))

# Fibonacci sequence

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a + b
        
gen_fibon(10)

for number in gen_fibon(10):
    print(number)

# Next function
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)
    
g = simple_gen()
print(next(g))
print(next(g))

# Iter function

s = 'hello'
for letter in s:
    print(letter)

next(s)

s_iter = iter(s)
next(s_iter)

# Homework


# Problem 1
def gensquares(N):
    for x in range(N):
          yield(x**2)

for x in gensquares(10):
    print(x)
    
# Problem 2
import random

random.randint(1, 10)

def rand_num(low, high, n):
    for x in range(n):
        yield(random.randint(low, high))

for num in rand_num(1, 10, 12):
    print(num)

# gencomp
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)


