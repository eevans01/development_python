#Programmer: Eric Evans, M.Ed.
#Program Name: Introducton to Queues
#Description: Working with FIFO Queues
#
from collections import deque #Imports the deque functionality from the collections library
myGuestList = deque(["Alice", "Betty", "Christy"]) #Creates a deque named myGuestList that is populated with the names Alice, Betty, & Christy
myGuestList.append("Darla") #Adds Darla to the deque (on the right)
myGuestList.append("Elizabeth") #Adds Elizabeth to the deque (on the right)
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.popleft() #Pops (removes) the item farthest to the left in the deque - in this case, that is Alice
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.popleft() #Pops (removes) the item farthest to the left in the deque - in this case, that is Betty
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.append("Ginger") #Adds Ginger to the deque (on the right)
myGuestList.append("Holly") #Adds Holly to the deque (on the right)
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.pop() #Pops (removes) the item farthest to the right in the deque
print(myGuestList) #Outputs the contents of the myGuestList deque
del myGuestList[2] #Deletes the item in index 2 in the deque - in this case, that is Elizabeth
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.insert(2,"Fran") #Adds Fran into the proper position - in this case, that is index 2
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.appendleft("Zara") #Adds Zara to the deque (on the left)
print(myGuestList) #Outputs the contents of the myGuestList deque
myGuestList.clear() #Clears the contents of the deque
print(myGuestList) #Outputs the contents of the myGuestList deque