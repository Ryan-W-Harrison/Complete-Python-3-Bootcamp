# Python class notes

# Lists
mylist = ["one", "two", "three"]
mylist[0]

mylist[1]
mylist[1:]

another_list = ['four', 'five']
new_list  = mylist + another_list

new_list[0] = new_list[0].upper()

new_list.append("six")
new_list.append("seven")

new_list.pop()

popped_item = new_list.pop()
new_list.pop(0)

new_list = ['a', 'e', 'x', 'b', "c"]
num_list = [4, 1, 8, 3]

my_sorted_list = new_list.sort()
type(my_sorted_list)

None

num_list
num_list.sort()
num_list.reverse()


# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

matrixI = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matrix2 = [matrix, matrixI]

# List comprehension
first_col = [row[0] for row in matrix]

[i[0] for i in matrix2]

# Dictionary
age_label = {"1" : "[0, 18)", "2" : "[18, 30)", "3" : "[30, 50)", "4" : "[50, 70)", "5" : "70+"}

age_label['1']
age_label['5']

age_label['6'] = "oldass"
age_label

age_label.keys()
age_label.values()
age_label.items()

# Tuples
t = (1, 2, 3)
mylist = [1, 2, 3]

type(t)
type(mylist)

len(t)
t = ('one', 2)
t[0]
t[-1]


t = ('a', 'a', 'b')
t.count('a')

t[0] = 'b'
mylist[0]  = "NEW"

# Sets
myset = set()
myset

myset.add(1)

myset.add(2)
myset
myset.add(2)

mylist = [1, 2, 3]*5
set(mylist)
mylist

# Booleans

1 > 2
1 == 1
1.0 == 1.0

with open('myfile.txt', mode = 'r') as myfile:
    contents = myfile.read()
    
1 < 2 < 3

1 < 3 > 2
1 == 1 < 2

not 1 == 1 < 2


# For loops
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import math as mathfor num in mylist:
    y = math.log(num, 10)
    print(y)
    
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
      print(f'Odd NUmber: {num}')

list_sum = 0

for i in mylist:
    list_sum = list_sum + i
    
    print(list_sum)

mystring = "Hellow World"

for letter in mystring:
    print(letter)
    
for _ in "Hello World":
    print("Cool")
    
    
tup = (1, 2, 3)
for j in tup:
    print(j)
    
list2 = [(2, 4), (6, 8), (10, 12)]

for i in list2:
    print(i)

for (t1, t2, t3) in list2:
    print(t2)
    
list2x = [(2, 4), (6, 8), (10)]

for i in list2:
    print(i)

for (t1, t2, t3) in list2:
    print(t2)
    
# Iterate dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

d.items()
d.keys()
d.values()

for k, v in d.items():
    print(k)
    print(v)

list(d.keys())

sorted(d.values())

remaining_classtime = [11, 16, 11, 2, 7, 174, 100, 81, 29, 46, 120, 18, 23, 17, 120, 23, 60, 40, 24, 45, 28, 3, 41, 45, 15, 1]

class_tot = sum(remaining_classtime) 

f'There are {class_tot // 60} hours and {class_tot % 60} minutes left'
f'There are {sum(remaining_classtime[0:4])  // 60} hours and {sum(remaining_classtime[0:4])  % 60} minutes left'


mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]

for a, b in mylist:
    print(a)

# Zen of Python
import this

# Print python version
import sys 
print(sys.version)

# While loops
x = 0
while 0 <= x < 5:
    print(f'The current value of x is {x}')
    x += 0.5
else:
  print(f'{x} is not less than 5')

# break, continue, pass
x = [1, 2, 3]
for item in x:
    # comment
    pass
  
print('end of my script')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

# Useful operators

mylist = [1, 2, 3]
# Range
for num in range(10):
    print(num)

for num in range(3, 10):
    print(num)

for num in range(0, 10, 2):
    print(num)
    
range(0, 11, 2) # prints nothing
list(range(0, 11, 2)) # need to cast to a list because it's a "generator"

# Ennumerate
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

index_count = 0
word = 'abcde'
for item in enumerate(word): # returns tuples
    print(item)
    
index_count = 0
word = 'abcde'
for index, letter in enumerate(word): # returns tuples
    print(index)
    print(letter)
    print('\n')
    
# zip - opposite of enumerate

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [10, 200, 300]

zip(mylist1, mylist2)
list(zip(mylist1, mylist2))
for item in zip(mylist1, mylist2):
    print(item)

for item in zip(mylist1, mylist2, mylist3):
    print(item)
    
mylist1 = [1, 2, 3, 4, 5, 6]    # additional items get ignored when zipping
for item in zip(mylist1, mylist2, mylist3):
    print(item)

# in operator
'x' in [1, 2, 3]
'x' in ['x', 'y', 'z']

'a' in 'a world'
'mykey' in {'mykey': 345}

d = {'mykey': 345}
345 in d.values()
345 in d.keys()

# min/max/random
mylist = [10, 20, 30, 40, 100]
min(mylist)
max(mylist)

from random import shuffle
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist) # in place function only
random_list = shuffle(mylist) # returns nothing
type(random_list)

from random import randint
randint(0, 100)
mynum = randint(0, 10)

# input
input('Enter a number here: ')
result = input('What is your name? ')
result

result = input('Favorite Number: ')
type(result) # always character ned to parse
float(result)
int(result)

# List comprehensions
lst = [x for x in 'word']
lst

lst = [x**2 for x in range(0, 11)]
lst

lst = [x for x in range(11) if x % 2 == 0]
lst

celsius = [0, 10, 20.1, 34.5, 100]
fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]
fahrenheit

celsius = [0, 10, 20.1, 34.5, 100]
def ctof(x) :
    y = ((9 / 5) * x + 32)
    return(y)


fahrenheit = [ctof(temp) for temp in celsius]
fahrenheit

lst = [ x**2 for x in [x**2 for x in range(11)] ]
lst

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
results

mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x * y)

results2 = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
results2

# Methods
lst = [1, 2, 3, 4, 5]

lst.append(6)
lst

# Functions - check notebook for more info

def say_hello():
    print("hello")
    
say_hello()

def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
  
check_even_list([1, 3, 7])

stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]

for ticker, price in stock_prices:
    print(price + (0.1 * price))
    
work_hours = [('Abby', 100), ("Billy", 400), ("Cassie", 800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for employee, work_hours in work_hours:
        if work_hours >= current_max:
            current_max = work_hours
            employee_of_month = employee
        else:
            continue
    
    # Return tuple 
    return (employee_of_month, current_max)

employee_check(work_hours)

# Function interactions chapter
example = [1, 2, 3, 4, 5, 6, 7]
from random import shuffle
shuffle(example)
example

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)

mylist = ["X", "O", "X"]
shuffle_list(mylist)

def player_guess():
    guess = ""
    while guess not in ["1", "2", "3"]:
        guess = input("Pick a number: 1, 2, or 3")
    return int(guess)
  
player_guess()

guess = player_guess()

def check_guess(mylist, guess):
    guess_index = guess - 1
    if mylist[guess_index] == "O":
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

# Initial list
mylist = ["X", "O", "X"]

# Shuffle list
mixedup_list = shuffle_list(mylist)

# user guess
guess = player_guess()

# check guess
check_guess(mixedup_list, guess)

text = "Levelheaded Llama"
text2 = text.upper()
text3 = text2.split()


text = "I am home"
text2 = text.split()
text3 = text2.reverse()
" ".join(text2)

(
  text.split()
      .reverse()
)

import re
x = [1, 3, 1]
y = ''.join([str(x) for x in x])
z = re.findall("33", y)

x = "Hello"
"".join([x*3 for x in "Hello"])

a,b,c = (9, 9, 9)

    sum1 = a + b + c
    sum2 = sum1 - 10
    a11 = a == 11
    b11 = b == 11
    c11 = c == 11
    any11 = a or b or c
    if sum1 <= 21:
        z = sum1
    elif sum1 > 21 and any11:
        z = sum2
    else:
        z = "BUST"
    return z
  
arr = [4, 5, 6, 7, 8, 9]

arr2 = list(filter(lambda x: x < 6 or x > 9, arr))

nums = [1, 2, 3, 0, 0, 7, 5]
    x1 = list(filter(lambda x: x == 0 or x == 7, nums))
    x2 = ''.join([str(x) for x in x1])
    x3 = re.findall("007", x2)
len(x3)

# map
def square(num):
  return num**2

my_nums = [1, 2, 3, 4, 5]
list(map(square, my_nums))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
      


mynames = ["John", "Cindy", "Sarah", "Kelly", "Mike"]
list(map(splicer, mynames))

# Filter
def check_even(num):
    return num % 2 == 0

nums = list(range(11))
list(filter(check_even, nums))


list(map(lambda num: num**2, my_nums))
list(filter(lambda n: n% 2 == 0, nums))

lambda s: s[::-1]
lambda x, y: x + y


locals()
print(locals())

# *args and **kwargs
def myfunc(*args):
    y = [x for x in args if x % 2 == 0]
    return y

myfunc(1, 2, 3, 4, 5, 6)

def alternate_cases(string):
    return ''.join([''.join(char.upper() if i%2 == 0 else char.lower() for i, char in enumerate(word)) for word in string.split()])
 
alternate_cases("Anthropomorphism")


# Function homework
import math    
def vol(rad):
    x = 4/3 * math.pi *rad**3
    return(x)
  
vol(2)

def ran_check(num, low, high):
    if low <= num <= high:
        x = "is"
    else:
        x = "is not"
    var = f'{num} {x} in the range between {low} and {high}'
    return(var)

ran_check(1, 2, 7)

x = "Hello Mr. Rogers, how are you this fine Tuesday?"
def up_low(s):
    upper = sum([x.isupper() for x in s])
    lower = sum([x.islower() for x in s])
    y = f'Upper: {upper}; Lower: {lower}'
    return(y)

up_low(x)


x = "nurses run"
def palindrome(s):
    s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]

palindrome(x)

palindrome("rise to vote sir")
palindrome("otto")
palindrome("meh")

import string
def ispangram(str1, alphabet = string.ascii_lowercase):
    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    str2 = set(str1)
    return sorted(alphabet) == sorted(str2.intersection(alphabet))

ispangram("The quick brown fox jumps over the lazy dog")
ispangram("Meh")

