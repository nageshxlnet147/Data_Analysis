"""
What is a string?

1. Definition 1
✓ A group of characters enclosed within single or double or triple quotes is called as string.

2. Definition 2
✓ We can say string is a sequential collection of characters.

3. String is more popular
✓ In any kind of programming language, mostly usage data type is string.

Creating string

Syntax 1: With single quotes
    name1 = 'Daniel'

Syntax 2: With double quotes
    name2 = "Daniel"

Syntax 3: With triple single quotes
    name3 = '''Daniel'''
"""
#Syntax 4: With triple double quotes
#    name4 = """Daniel"""


s1 = 'Nagesh'
s2 = "Nagesh"
s3 = '''Nagesh'''
s4 = """Nagesh"""

print(s1, s2, s3, s4)

# file:///home/coder147/Pictures/Screenshots/Screenshot%20from%202026-03-28%2020-54-22.png

# Accessing string by using index

a1 = "Data_Science"
print(a1[3])

print()

# Accessing string by using slicing

print(a1[1:7])

print()

# Accessing string by using for loop

for i in a1:
    print(i)

print()

"""
1. Mutable
✓ Once if we create an object then the state of existing object can be change/modify/update.
✓ This behaviour is called as mutability.

2. Immutable
✓ Once if we create an object then the state of existing object cannot be change/modify/update.
✓ This behaviour is called as immutability.

3. Strings are immutable
✓ String having immutable nature.
✓ Once we create a string object then we cannot change or modify the existing object.
"""
try:
    a2 = "Data"
    a2[1] = 'e'
except Exception as e:
    print(e)

print()

"""
Mathematical operators on string objects
✓ We can perform two mathematical operators on string.
✓ Those operators are,
o Addition (+) operator.
o Multiplication (*) operator.

1. Addition (+) operator with string
✓ The + operator works like concatenation or joins the strings.

2. Multiplication (*) operator with string
✓ This operator works with string to do repetition.
"""

st1 = 'Data'
st2 = "Science"

print(st1+st2)

print(st1*3, st2*3)

print()

"""
Length of the string
✓ We can find number of characters in string by using len() function
"""

st3 = "Data_Science"

print(len(st3))

print()

"""
Membership operators (in, not in)

Definition 1
✓ We can check, if a string or character is a member of string or not by using in and not in operators

Definition 2
✓ We can check, if string is a substring of main string or not by using in and not in operators.

1. in operator
✓ in operator returns True, if the string or character found in the main string.

2. not in operator
✓ The not in operator returns opposite result of in operator.
✓ not in operator returns True, if the string or character not found in the main string.
"""

op1 = "Data_Science"

print('Data' in op1)
print('sceince' not in op1)

print()

print(dir(str))

"""
Methods in str class
✓ As discussed, str is a predefined class.
✓ So, str class can contain methods because methods can be created inside of class only.
✓ We can check these methods by using dir(parameter1) predefined function.
✓ So, internally str class contains two types of methods,
    o With underscore symbol methods.
        ▪ We no need to focus
    o Without underscore symbol methods.
        ▪ We need to focus much on these
        [capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

Important point
✓ As per object-oriented principle,
    o If we want to access instance methods, then we should access by using object name.
✓ So, all str class methods we can access by using str object
"""

# This method converts lower case letters into upper case letters

up1 = "data_science"
print(up1.upper())

print()

# This method converts upper case letters into lower case letters

up2 = "DATA_SCIENCE"
print(up2.lower())

print()

# This method removes left and right side spaces of string

up3 = "   Data_Science    "
print(up3.strip())

print()

# By using count() method we can find the number of occurrences of substring present in the string

up4 = "Data science is good and Data analysis is part of big Data"
print(up4.count("Data"))

print()

# We can replace old string with new string by using replace(p1, p2) method

up5 = "Python scienece is future"
up6 = up5.replace("Python", "Data")
print(up5)
print(up6)
print(id(up5))
print(id(up6))

"""
Replace method returns new string object
✓ As we know string is immutable, so replace(p1, p2) method never perform changes on the existing string object.
✓ replace(p1, p2) method creates new string object, we can check this by using id(p) function
"""

print()

"""
Splitting of Strings:

✓ The default separator is space.
✓ We can split the given string according to specified separator by using
split(p) method.
✓ split(p) method returns list.
"""

up7 = "Nagesh"
up8 = up7.split()
print(up7)
print(up8)

