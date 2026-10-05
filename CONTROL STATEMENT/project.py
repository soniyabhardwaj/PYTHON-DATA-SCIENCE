#users choice 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")
if choice == '+':
    result = num1 + num2
    print("Result:", result)
elif choice == '-':
    result = num1 - num2
    print("Result:", result)
elif choice == '*':
    result = num1 * num2
    print("Result:", result)    
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")    
        