#nested loop 
'''for i in range(1, 4):  # outer loop
    for j in range(1, 4):  # inner loop
        print(f"i: {i}, j: {j}")


#break
#The break statement is used to exit a loop prematurely when a certain condition is met. It allows you to terminate the loop and continue with the next statement after the loop.
for i in range(1, 6):
    if i == 3:
        break  # exit the loop when i is equal to 3
    print(i) '''

#continue
#The continue statement is used to skip the rest of the code inside
#  a loop for the current   
# iteration and move on to the next iteration. It allows you to bypass certain iterations based on a condition.
for i in range(1, 6):
    if i == 3:
        continue  # skip the rest of the code for i equal to 3
    print(i)


#pass
# The pass statement is a placeholder that does nothing. It is used when a statement is syntactically required but you don't want to execute any code. It allows you to create empty blocks of code without causing errors.

                    