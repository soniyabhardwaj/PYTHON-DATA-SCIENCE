'''loops in python
multiple times execution of a block of code until a certain condition is met.
for loop: used to iterate over a sequence (such as a list, tuple, string)'''


#1- while loop: used to repeatedly execute a block of code as long as a certain condition is true.   
#2- for loop: used to iterate over a sequence (such as a list, tuple, string)
#or other iterable objects. It executes a block of code for each item in the sequence.

#-----------------------
""" while loop syntax:
i = 1
while i<= 5:
    print(i)
    i += 1 """ 

a = [1, 2, 3, 4, 5]
for item in a:
    print(item) 

#range function: generates a sequence of numbers within a specified range. It is commonly used in for loops to iterate over a specific number of times.
#syntax: range(start, stop, step)    
a = list(range(1, 6))
print(a)
  # generates numbers from 1 to 5 (stop is exclusive)