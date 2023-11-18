#class-notes_modules.py
from collections import Counter
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]

Counter(mylist)

mylist = ['a', 'a', 10, 10, 10]
Counter(mylist)

sentence = 'How many times does each word show up in this sentence with a word'
Counter(sentence.lower().split())

letters = 'aaabbbbccccccdddddddddd'
c = Counter(letters)

c.most_common()
c.most_common(n=3)

sum(c.values())
len(c)
c.clear()
list(c)
set(c)
dict(c)
type(c)
c.items()
#c.most_common()[:-n-1:-1]
c.most_common()[:-4:-1]

c += Counter()

# Default dictionary
from collections import defaultdict
d = {'a':10}
d
d['a']
d['WRONG']

d = defaultdict(lambda: 0)
d['correct'] = 100
d['correct']
d['WRONG KEY!']

# Named tuple
mytuple = (10, 20, 30)
mytuple[0]

from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age = 5, breed = 'Husky', name = 'Sam')
type(sammy)
sammy
sammy.age
sammy.breed
sammy.name
sammy[0]

#------------------
# OS module
#-----------------
f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

import os
os.getcwd()
os.listdir()

xx = os.listdir()

import shutil

shutil.move('practice.txt', '/home/rharrison/projects')

os.unlink(path)
os.rmdir(path)
shutil.rmtree(path) # careful

import send2trash # send to trash bin incase
send2trash.send2trash('practice.txt')

# cd ~/.local/share/Trash


for folder, sub_folders, files in os.walk('/home/rharrison/projects/Complete-Python-3-Bootcamp/12-Advanced Python Modules/Example_Top_Level'):
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
    # Now look at subfolders

# Send commands to terminal directly
os.system("pip install scikit-learn")

# Date/time module
import datetime
mytime = datetime.time(2, 20)
mytime.minute
mytime.hour

print(mytime)

mytime = datetime.time(13, 20, 1, 20)
print(mytime)

today = datetime.date.today()
print(today)

today.year
today.month
today.day
today.ctime()

from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)

mydatetime = mydatetime.replace(year = 2020)
print(mydatetime)

# DATE
from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
date_diff = date1 - date2
print(date_diff)

date_diff.days

dt1 = datetime(2021, 11, 3, 22, 0)
dt2 = datetime(2020, 11, 3, 12, 0)
dt_diff = dt1 - dt2
print(dt_diff)

dt_diff.days
dt_diff.microseconds
dt_diff.seconds
dt_diff.total_seconds()

# Math and Random modules
import math
help(math)

value = 4.35
math.floor(value)
math.ceil(value)
round(value)

math.pi
math.e
math.inf
math.nan

math.log(math.e)

math.log(100, 10)
math.log(10, 10)
math.sin(10)
math.degrees(math.pi/2)
math.radians(180)
math.pi

import random
random.randint(0, 100)

random.seed(101)
print(random.randint(0, 100))


mylist = list(range(0, 20))
mylist
random.choice(mylist)


# Sample with replacement
random.choices(population = mylist, k = 10)

# Sample without replacement
random.sample(population = mylist, k = 10)

random.shuffle(mylist)

random.uniform(a = 0, b = 100)
random.gauss(mu = 0, sigma = 1)

# Debugging
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)

# Regex section

text = "The agen't phone number is 408-555-1234. Call soon!"
'phone' in text

import re
pattern = 'phone'
match = re.search(pattern, text)

pattern2 = "NOT IN TEXT"
re.search(pattern2, text)

match
match.span()
match.start()
match.end()

text = 'my phone once, my phone twice'
match = re.search('phone', text)
match
matches = re.findall('phone', text)
matches
len(matches)
for match in re.finditer('phone', text):
    print(match)
    print(match.span())
    print(match.group())
    
r'mypattern\d'

text = "My telephone number is 408-555-1234"
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
phone.group()

phone = re.search(r'\d+-\d+-\d+', text)
phone.group()

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
results.group()
results.group(1)
results.group(2)
results.group(3)

# Or operator
re.search(r'man|woman', "This man was here.")
re.search(r'man|woman', "This woman was here.")

re.findall(r'..at', 'The cat in the hat went splat.')
re.findall(r'\S+at', 'The cat in the hat went splat.')

re.findall(r'^\d', '1 is a number')
re.findall(r'\d$', '1 is a number, also is 2')

phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
re.findall(pattern, phrase)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

re.findall(r'[^!.? ]+', test_phrase)

clean = ' '.join(re.findall('[^!.? ]+', test_phrase))


text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
re.findall(r'[\w]+-[\w]+', text)

# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

re.search(r'cat(fish|nap|claw)', text)
re.search(r'cat(fish|nap|claw)', texttwo)
re.search(r'cat(fish|nap|claw)', textthree)

# Module puzzle

import os
cwd = os.getcwd()
dir_zip = f'{cwd}/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise'

file_zip = f'{dir_zip}/unzip_me_for_instructions.zip'

import shutil

shutil.unpack_archive(filename = file_zip, extract_dir = dir_zip, format = 'zip')

# Good work on unzipping the file!
# You should now see 5 folders, each with a lot of random .txt files.
# Within one of these text files is a telephone number formated ###-###-#### 
# Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
# Good luck!

# Pattern to search
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
#results = re.search(phone_pattern, text)
text = None
results = []

def search(file, pattern = phone_pattern):
    f = open(file, 'r')
    text = f.read()
    
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

for folder, sub_folders, files in os.walk(f'{dir_zip}/extracted_content'):
    for f in files:
        full_path = f'{folder}/{f}'
        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())

        
xx = list(os.walk(f'{dir_zip}/extracted_content'))

xx[0]
xx[1]

