#Programmer: Eric Evans, M.Ed.
#Program Name: 4-Function Calculator - V4
#Description: 4-Function Calculator with Error Checking
runAgainUpper = "Y" #Creates a variable named runAgainUpper with a value of Y
while runAgainUpper != "N": #Starts a while loop that runs as long as the variable named runAgainUpper does not equal N
  print("***************************")
  print("** 4-Function Calculator **")
  print("**                       **")
  print("** A - Addition          **")
  print("** S - Subtraction       **")
  print("** M - Multiplication    **")
  print("** D - Division          **")
  print("***************************")
  menu_choice = input("Enter the letter of the function you would like to do and press ENTER:") #Asks the user which menu option they would like
  #Addition Function
  if menu_choice in['A','a']: #Conditional statement looking is user entered A or a from the menu.
    while True: #Starts a while loop that runs as long as true
      try: #
        a1 = float(input("Enter the first number you would like to add and press ENTER:"))
        a2 = float(input("Enter the second number you would like to add and press ENTER:"))
      except ValueError:
        print("")
        print("**WARNING** Invalid Entry Made! Please try Again.")
        print("")
      else:
        aanswer = a1 + a2
        print(aanswer)
        break
  #Subtraction Function
  elif menu_choice in['S','s']:
    while True:
      try:
        s1 = float(input("Enter the big number you want to subtract from and press ENTER:"))
        s2 = float(input("Enter the smaller number you want to subtract from the first number and press ENTER:"))
      except ValueError:
        print("")
        print("**WARNING** Invalid Entry Made! Please try Again.")
        print("")
      else:
        sanswer = s1 - s2
        print(sanswer)
        break
  #Multiplication Function
  elif menu_choice in['M','m']:
    while True:
      try:
        m1 = float(input("Enter the first number you want to multiply and press ENTER:"))
        m2 = float(input("Enter the second number you want to multiply and press ENTER:"))
      except ValueError:
        print("")
        print("**WARNING** Invalid Entry Made! Please try Again.")
        print("")
      else:
        manswer = m1 * m2
        print(manswer)
        break
  #Division Function
  elif menu_choice in['D','d']:
    while True:
      try:
        d1 = float(input("Enter the total number of items you have that you want to divide and press ENTER:"))
        d2 = float(input("Enter the total number of equal-sized groups you want to be divided into and press ENTER:"))
      except ValueError:
        print("")
        print("**WARNING** Invalid Entry Made! Please try Again.")
        print("")
      else:
        danswer = d1 / d2
        print(danswer)
        break
  #Default Function
  else:
    print("***********************")
    print("** Invalid Selection **")
    print("** Exiting Program   **")
    print("** Please Try Again  **")
    print("***********************")
  runAgain = input("Do You Want to Run Again? [Y] or [N]")
  runAgainUpper = runAgain.upper()
print("Exiting Program")
print("Thank You!")