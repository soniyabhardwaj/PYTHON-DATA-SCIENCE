name = 'John'
name = "John"
print(name)

'''1 immutuable types: cannot be changed after creation.
 Examples include strings, tuples, and frozensets.'''
'''2 indexed types: allow you to access individual elements using an index or key. 
Examples include strings, lists, tuples, and dictionaries.
indexing = 0 , +ve , -ve 
3 iterable types: can be looped over using a for loop or other iteration methods.
Examples include strings, lists, tuples, sets, and dictionaries.'''
#positive indexing left  to right 0,1,2,3,4,5
a = "Hello, World!"
print(a[1])  # Output: e

#negative indexing right to left -1,-2,-3,-4,-5
a = "Hello, World!"
print(a[-1])  # Output: !

#iterable
for char in a:
    print(char)  # Output: H, e, l, l, o, ,,  , W, o, r, l, d, !

#operation on string
str1 = "Hello"
str2 = "World"      
str3 = str1 + " " + str2
print(str3)  # Output: Hello World
length = len(str3)
print(length)  # Output: 11
text = "Hello, World!"
print(text[1:5])  # Output: ello
#slicing
print(text[7:12])  # Output: World
print(text[ : : -1]) # Output: !dlroW ,olleH
#reapeat
num1 = "Hello"
num2 = "World"
result = num1 * 3
#checking membership
if "Hello" in result:
    print("Hello is present in the result.")  # Output: Hello is present in the result. 
if "Python" not in result:
    print("Python is not present in the result.")  # Output: Python is not present in the result.   

str.upper()
str.lower()
str.capitalize()   #first letter capital
str.title()        #first letter of each word capital
str.swapcase()     #swap case

#find() - returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
Example: text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7
#replace() - returns a new string with all occurrences of a substring replaced with another substring.
Example: text = "Hello, World!" 
new_text = text.replace("World", "Python")
print(new_text)  # Output: Hello, Python!

#split() - splits a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.
Example: text = "Hello, World!"
substrings = text.split(", ")
print(substrings)  # Output: ['Hello', 'World!']

#join() - joins a list of strings into a single string, using a specified delimiter.
Example: substrings = ['Hello', 'World!']
result = ", ".join(substrings)
print(result)  # Output: Hello, World!

#checking if a string starts or ends with a specific substring:
text = "Hello, World!"  
print(text.startswith("H"))  # Output: True
print(text.endswith("m"))   # Output: false

