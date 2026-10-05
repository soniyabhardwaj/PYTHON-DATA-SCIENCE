''' operators
    PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) is a set of rules that defines the order of operations for mathematical expressions. It ensures that calculations are performed in a consistent manner, allowing for accurate results.
    arithmetic operators: +, -, *, /, %, **, //
'''
print("Arithmetic Operators:")
a = 10
b = 3
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Modulus:", a % b)         # Modulus
print("Exponentiation:", a ** b) # Exponentiation
print("Floor Division:", a // b) # Floor Division

# floor division operator returns the largest integer less than or equal to the result of the division. It discards the decimal part and gives you the whole number quotient.   
#modulus operator returns the remainder of a division operation. It gives you the value that is left over after dividing one number by another.
#exponentiation operator raises a number to the power of another number. It calculates the result of multiplying the base number by itself a certain number of times, as specified by the exponent.

'''comaparison operators: ==, !=, >, <, >=, <=
boolean values: True or False'''
x = 10
y = 5
print("Equal:", x == y)          # Equal
print("Not Equal:", x != y)      # Not Equal
print("Greater Than:", x > y)    # Greater Than
print("Less Than:", x < y)       # Less Than
print("Greater Than or Equal:", x >= y)  # Greater Than or Equal
print("Less Than or Equal:", x <= y)     # Less Than or Equal


'''logical operators: and, or, not
logical operators are used to combine multiple conditions
 r expressions and evaluate them to produce a single boolean result
AND - returns True if both conditions are True, otherwise returns False.
OR - returns True if at least one of the conditions is True, otherwise returns False.
NOT - returns the opposite boolean value of the condition. If the condition is True, it returns False, and if the condition is False, it returns True.'''

print ("Logical Operators:")
a = True
b = False
print("AND:", a and b)  # AND
print("OR:", a or b)    # OR
print("NOT:", not a)    # NOT

'''assignment operators: =, +=, -=, *=, /=, %=, **=, //=
assignment operators are used to assign values to variables. 
They allow you to perform operations on a variable
 and update its value in a concise manner.
 '''
x = 10
print("Assignment Operators:")
print("x =", x)
x += 5
print("x += 5:", x)
x -= 3
print("x -= 3:", x)
x *= 2
print("x *= 2:", x)
x /= 4
print("x /= 4:", x)

'''identity operators: is, is not
identity operators are used to check if two variables refer to the same object in memory.
is - returns True if both variables refer to the same object, otherwise returns False.
is not - returns True if the variables refer to different objects, otherwise returns False.'''
a = 5
b = 5
c = 10
print("a is b:", a is b)      # True
print("a is not b:", a is not b)  # False
print("a is c:", a is c)      # False

'''membership operators: in, not in'''
list = [1, 2, 3, 4, 5]
print("3 in list:", 3 in list)        # True
print("6 not in list:", 6 not in list)  # True