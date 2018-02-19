#Programmer Name: Eric Evans
#Program Name: Greetings
runagain = "Y"
while runagain == "Y" or runagain == "y":
    user_name = input("Please Enter Your Name and Press ENTER: ")
    print("")
    print("Hello" + " " + user_name)
    runagain = input("Run Program Again? [Y]es or [N]o and Press ENTER")
print("")
print("Thank You")