#Programmer: Eric Evans, M.Ed.
#Program Name: 4-Function Calculator
#Description: 4-Function Calculator in Python
print("***************************")
print("** 4-Function Calculator **")
print("**                       **")
print("** A - Addition          **")
print("** S - Subtraction       **")
print("** M - Multiplication    **")
print("** D - Division          **")
print("***************************")
menu_choice = input("Enter the letter of the function you would like to do and press ENTER:")
#Addition Function
if menu_choice in['A','a']:
  a1 = float(input("Enter the first number you would like to add and press ENTER:"))
  a2 = float(input("Enter the second number you would like to add and press ENTER:"))
  aanswer = a1 + a2
  print(aanswer)
#Subtraction Function
elif menu_choice in['S','s']:
  s1 = float(input("Enter the big number you want to subtract from and press ENTER:"))
  s2 = float(input("Enter the smaller number you want to subtract from the first number and press ENTER:"))
  sanswer = s1 - s2
  print(sanswer)
#Multiplication Function
elif menu_choice in['M','m']:
  m1 = float(input("Enter the first number you want to multiply and press ENTER:"))
  m2 = float(input("Enter the second number you want to multiply and press ENTER:"))
  manswer = m1 * m2
  print(manswer)
#Division Function
elif menu_choice in['D','d']:
  d1 = float(input("Enter the total number of items you have that you want to divide and press ENTER:"))
  d2 = float(input("Enter the total number of equal-sized groups you want to be divided into and press ENTER:"))
  danswer = d1 / d2
  print(danswer)
#Default Function
else:
  print("***********************")
  print("** Invalid Selection **")
  print("** Exiting Program   **")
  print("** Please Try Again  **")
  print("***********************")