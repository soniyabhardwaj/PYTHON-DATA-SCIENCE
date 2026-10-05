#list helps to collect multiple values in a single variable. It is an ordered, mutable, and allows duplicate elements.
#list is defined using square brackets [] and elements are separated by commas. 
name = "soniya"
age = 20
marks = 21

my_list = [name, age, marks]
print(my_list)  # Output: ['soniya', 20, 21] 

#features of list:
#1- ordered: the order of elements in a list is preserved, and you can access
#elements using their index.
#2- mutable: you can modify the elements of a list after it is created.
#3- allows duplicate elements: a list can contain multiple occurrences of the same value.
#4- heterogeneous: a list can contain elements of different data types, such as integers, strings, floats, etc.


#ways to create a list:
#1- using square brackets []
my_list1 = [1, 2, 3, 4, 5]
print(my_list1)  # Output: [1, 2, 3, 4, 5]

#2- using the list() constructor
my_list2 = list((1, 2, 3, 4, 5))
print(my_list2)  # Output: [1, 2, 3, 4, 5]  

#updating list elements:
my_list1[0] = 10
print(my_list1)  # Output: [10, 2, 3, 4, 5]

#slicing a list:
my_list3 = [1, 2, 3, 4, 5]
print(my_list3[1:4])  # Output: [2, 3, 4]

#concatenation of lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

#repetition of lists:
list3 = [1, 2, 3]
result = list3 * 3
print(result)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#membership testing:
my_list4 = [1, 2, 3, 4, 5]
if 3 in my_list4:
    print("3 is present in the list.")  # Output: 3 is present in the list.

#copying a list:
#1- using the copy() method
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3, 4, 5]


#append : add at the end 
a = [1,2,3] 
a.append(4)
print(a)

#extend :  add two list 
a = [1,2,3] 
b = [3,4,5]
a.extend(b)
print(a) #output = [1,2,3,3,4,5]

#insert : add acc to choice 
a = [1,2,3] 
a.insert(1, soniya)
print(a)

#remove :element
a = [1,2,3] 
a.remove(1)
print(a)

#popped : index
a = [1,2,3] 
a.pop(0)
print(a)

#clear : clears whole list
#index : tell index of the element 
#count : tell how many times th element is there
#sort: sort the list
#reverse : reverse the list
