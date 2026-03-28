# Sequential statement : Its execute top to bottom

print("one")
print("two")
print("three")

print()
"""
Conditional or Decision-making statements

✓ if is a keyword in python
✓ if statement contains an expression/condition/value.
✓ As per the syntax colon (:) is mandatory otherwise it throws syntax error.
✓ After if statement we need to follow indentation otherwise it throws
IndentationError.
✓ Condition gives the result as a bool type, means either True or False.
✓ If the condition result is True, then if block statements will be executed
✓ If the condition result is False, then if block statements won’t execute.
"""

# if statement 

i = 10
if i > 9:
	print("Yes")

print()

"""
✓ if and else are keywords in python
✓ if statement contains an expression/condition.
✓ As per the syntax colon (:) is mandatory otherwise it throws syntax error.
✓ After if and else statements we need to follow indentation otherwise it
throws IndentationError.
✓ Condition gives the result as bool type, means either True or False
✓ If the condition result is True, then if block statements will be executed
✓ If the condition result is False, then else block statements will be
executed.
"""
# if else statement

if i < 20:
	print("Yes")
else:
	print("No")
print()

"""
✓ if, elif and else are keywords in python
✓ if statement contains an expression/condition.
✓ As per the syntax colon (:) is mandatory otherwise it throws error.
✓ After if, elif and else statements we need to follow indentation
otherwise it throws IndentationError.
✓ Condition gives the result as bool type, means either True or False
✓ If the condition result is True, then any matched if or elif block
statements will execute.
✓ If all if and elif conditions results are False, then else block statements
will execute.
"""
# if elif statement

if i > 20:
	print("grater")
elif i < 20:
	print("Less than")
else:
	print("Equal")

print()

"""
Looping
✓ If we want to execute a group of statements in multiple times, then we
should go for looping kind of execution.
o for loop
o while loop

for loop
✓ for is a keyword in python
✓ Basically, for loop is used to get or iterate elements one by one from
sequence like string, list, tuple, etc…
✓ While iterating elements from sequence we can perform operations on
every element.
"""
# for loop 

for i in range(1, 10):
	print(i)

print()

"""
✓ while is a keyword in python
✓ If we want to execute a group of statements repeatedly until the
condition reaches to False, then we should go for while loop.
✓ while loop contains an expression/condition.
✓ As per the syntax colon (:) is mandatory otherwise it throws syntax error.
✓ After while loop we need to follow indentation otherwise it throws
IndentationError.
✓ Condition gives the result as bool type, means either True or False
✓ If the condition result is True, then while loop executes till the condition
reaches to False.
✓ If the condition result is False, then while loop execution terminates.
"""
# while loop

x = 1 
while x <= 10:
	print(x)
	x += 1	

print()

"""
break statement
✓ break is a keyword in python
✓ The break statement can be used inside the loops.
✓ By using break we can break the execution based on some condition.
✓ Generally, break statement is used to terminate for and while loops.
"""

# break statement

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print()

"""
continue statement
✓ continue is a keyword in python
✓ We can use continue statement to skip current iteration and continue
next iteration.
"""

# continue statement

for i in range(1, 10):
    if i == 6:
        continue
    print(i)

print()

"""
✓ pass is keyword in python.
✓ The pass statement is used as a placeholder for future code.
✓ It is useful as a placeholder when a statement is required syntactically,
but no code needs to be executed.
✓ pass is a null operation, when it is executed, nothing happens.
✓ We can define an empty function, class, method with pass statement.
"""

# pass statement 

for i in range(1, 10):
    pass

