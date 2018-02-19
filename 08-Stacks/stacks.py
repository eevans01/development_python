#Programmer: Eric Evans, M.Ed.
#Program Name: Introducton to Stacks
#Description: Working with LIFO Stacks, For Loops, and Conditional Statements
#
stack_ascending = [1, 2, 3, 4, 5] #Create ascending stack with integers 1, 2, 3, 4, & 5
stack_ascending.append(6) #Appends 6 to the top of the stack
stack_ascending.append(7) #Appends 7 to the top of the stack
stack_ascending.append(8) #Appends 8 to the top of the stack
print ("Ascending Stack: " + stack_ascending) #Print the contents of the ascending stack
stack_descending = [] #Creates an empty stack named stack_descending to hold the descending integers
for x in range(0,8): #Opens a for loop that will run 8 times
  stack_descending.append(stack_ascending.pop()) #Populates the descending stack with the top item of the ascending stack
print ("Descending Stack: " + stack_descending) #Print the contents of the descending stack
stack_even = [] #Creates an empty stack named stack_even to hold even integers
stack_odd = [] #Creates an empty stack named stack_odd to hold odd integers
for x in range(0,8): #Opens a for loop that will run 8 times
  top = stack_descending.pop() #Defines a variable named top that holds the value from the top of the descending stack
  if top%2 == 0: #Determines if modulus 2 of the top variable is equal to zero
    stack_even.append(top) #If modulus 2 of the top variable is equal to zero, the value is populated to the stack_even
  else: #Catch all
    stack_odd.append(top) #If modulus 2 of the top variable is NOT equal to zero, the value is populated to the stack_odd
print ("Even Integers Stack: " + stack_even) #Print the contents of the even stack
print ("Odd Integers Stack: " + stack_odd) #Print the contents of the odd stack