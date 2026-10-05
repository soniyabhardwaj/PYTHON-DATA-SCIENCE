a = [1,2,3,4,5,6,7,8,9,34,4,]
print(min(a))
print(max(a))

#common
a = [1,2,3,4,5,6]
b  =  [7,8,9,34,4,]

#set func
s1 = set(a)
s2 = set(b)
s3 = s1.interaction(s2)
print(list(s3))

#nested list 
a = [1,2,3]
b = [1,2,3,4,[a,3,5]]
print (b)

#creating list withh help of range 
number = list(range(1,12,1))
print(number)

#list comprehension
squares = [i ** 2 for i in range(1,11) if i%2 == 0]
print(squares)