"""
Functions - Part - 1

1. Function
	✓ A function can contain group of statements which performs the task.

Advantages
	✓ Maintaining the code is an easy way.
	✓ Code reusability.

Make a note
	✓ print() is predefined function in python which prints output on the console.

2. Types of function
	✓ There are two types of functions,
		o Pre-defined or built-in functions
		o User-defined functions
3. Pre-defined or built-in functions
	✓ The functions which are already existing in python are called as predefined function
	Examples
		o print(p)
		o type(p)
		o input(p)

4. User Defined Functions:
	✓ Based on requirement a programmer can create his own function, these functions are called as user defined functions.
	✓ So, practically we will see how to define and use, user defined functions.

5. Function related terminology
	✓ If we want to understand function concept in better way then we need to focus on function related terminology,
		o def keyword
		o name of the function
		o parenthesis ()
		o parameters (if required)
		o colon symbol:
		o function body
		o return type (optional)

6. Function definition
	✓ A function can contains group of statements.
	✓ The purpose of function is to perform an operation.
	✓ A function can contain mainly two parts,
		1. Creating a function
		2. Calling a function

	6.1. Creating a function
		✓ Very first step is we need to create a function.
		✓ We need to use def keyword to create a function.
		✓ After def keyword we should write name of the function.
			o After function name, we should write parenthesis ()
				o This parenthesis may contain parameters.
				▪ Parameters are just like variables which receive the values
				▪ If function having parameters, then we need to provide the values while calling.
				▪ We will learn more in parameterized function
			o After parenthesis we should write colon : symbol
			o After : symbol in next line we should provide indentation
	✓ Function body.
		o Actual logic contains by function body
		o This function body helps to perform the operation.
	✓ Before closing the function, function may contain return type.

            Syntax
                def functionname():
                	"doc string"
                	Body of the function to perform operation

    A naming convention to define a function
	    ✓ As discussed in Naming convention chapter, function name should be in lower case.
    	✓ If name having multiple words, then separating words with underscore (_) symbol is a good practice.

    6.2 Calling a function
        ✓ After function is created then we need to call that function to execute the function body.
        ✓ While calling the function, function name should be match otherwise we will get error.

"""

# Function creation and calling

def first_function():
    print("First function creation")

first_function()

print()

# Creating two functions and calling those functions

def first():
    print("First Fun")

def second():
    print("Scenod fun")

first()
second()

print()

"""
A Function can call other function
    ✓ Based on requirement a function can call another function as well.
    ✓ We can call a function inside another function.

"""


def second():
    print("Function can call other function")
    first()
second()

print()

"""

Based on Parameters: Functions are two types
	✓ Based on parameters, functions can be divided into two types,
		o Function without parameters (or) No parameterised function
		o Function with parameters (or) Parameterised function
1. Function without parameters
	✓ If a function having no parameters then that function is called as, No parameterized function
	Syntax
		def nameofthefunction():
			body of the function to perform operations
			function calling
2.Function with parameters
	✓ If a function having parameters then that function called as parameterised function

Why function having parameters?
	✓ Function parameters help to process the function operation.
	✓ When we pass parameters then,
		o Function capture parameters values
		o These values perform the operations.
		o Finally it brings the result.
	Syntax
		def functionname(parameter1, parameter2, …):
			body of the function
			function calling

"""

# Function without parameters:

def with_out_parameter():
    print("with out parameterised function")
with_out_parameter()

print()

# Function with parameters:

def with_parameter(a):
    print("With parameterised function", a)
with_parameter(10)

print()

def testing(a):
    print("one parameterised function:", a)
x = input("Enter a value:")
testing(x)

print()

def testing(a, b):
    print("two parameterised function:", a, b)
testing(10, 20)

print()

"""

return keyword in python
	✓ Based on return statement, functions can be divided into two types,
		o Function without return statement
		o Function with return statement
	✓ return is a keyword in python.
	✓ We should use return statement with function or method, otherwise we will get error.
	✓ It’s not mandatory to write return statement to a function.
	✓ A function without return statement is valid.
    ✓ A method can return a value as well.

Syntax:
    def nameofthefunction():
        body of the function
        return result

Why we need to assign a function calling to a variable?
    ✓ If we assign function calling to a variable then that variable holding the variable value.
    ✓ That variable we can use further in our program.
"""

def function_ret(a):
    print("function return type", a)
    return a

b = function_ret(10)
print(b)

print()

# Function with return statement:

def balance():
    return 0

b = balance()

if b == 0:
    print("Balance is: ", b)
elif b<=0:
    print("Balance is: ", b, " negative please deposit")
else:
    print("Balance is: ", b)

print()

"""

return vs None
✓ If any function is not return anything, then by default that function
returns None data type.
✓ We can also say as, if we are not writing return statement, then default
return value is None

"""

def func():
    print("func calling")

f1 = func()
print(f1)

print()

"""

A function can return multiple values
    ✓ In python, a function can return multiple values.
    ✓ Based on requirement a function can return multiple values.
        o If function is returning two values then while function calling we need to assign to two variables
        o If function is returning three values then while function calling we need to assign to three variables.
        o If function is returning more than one values, while calling function if we assign with one variable then all values will be stored in tuple.

Syntax:
    def name_of_the_function():
        body of the function
        return value1, value2, value3,...,valueN

"""

# Define a function which can return multiple values

def m1():
    a = 10
    b = 11
    return a, b

x, y = m1()
print("first value is:", x)
print("second value is:", y)

print()

# Define a function which can return multiple values

def m1():
    a = 10
    b = 11
    c = 12
    return a, b, c

x, y, z = m1()
print("first value is:", x)
print("second value is:", y)
print("third value is:", z)

print()

# Define a function which can return multiple values

def m1():
    a = 10
    b = 11
    c = 12
    return a, b, c

x = m1()
print("all values:", x)

print()


