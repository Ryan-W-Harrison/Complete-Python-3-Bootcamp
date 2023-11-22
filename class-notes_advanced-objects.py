# class-notes_advanced-objects.py
hex(246)
bin(1234)
hex(16)
hex(15)

pow(2, 3)
pow(2, 4, 3)


abs(-3.14)

round(395.125, 2)
round(396.125, 2)
round(396.1234, -1)
round(396.1234, -2)

# Strings
s = 'hello world'

s.capitalize()

s.upper()
s.lower()

s.count('o')
s.find('o')

s.split('e')
s.partition('e')

# Sets
s = set()

s.add(1)
s.add(2)

s.clear()
s

s = {1, 2, 3}
sc = s.copy()
s.add(4)
s
sc

s.difference(sc) # assymetric

s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
s1
s2

s.discard(2)
s

s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.intersection(s2)
s1

s1.intersection_update(s2)

