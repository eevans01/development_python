#Programmer Name: Eric Evans, M.Ed.
#Program Name: Casting and Strings
#Program Description: Working with Casting Floats and Manipulating Strings
#
#Declaration of variables.
myDecimalNumber = 79.95
myString = "Ferris High School"
print("My Decimal Number = ")
print(myDecimalNumber)
myDecimalNumberAsString = str(myDecimalNumber)
print("My Decimal Number = " + myDecimalNumberAsString)
myDecimalNumberAsInteger = int(myDecimalNumber)
myDecimalNumberAsIntegerString = str(myDecimalNumberAsInteger)
print("My Decimal Integer = " + myDecimalNumberAsIntegerString)

print(myString)
print(myString * 2)
print(myString[0])
print(myString[1:8])
print(myString[10:])
print(myString[:10])
myNumberOfIs = myString.count("i")
print(myNumberOfIs)

myStringLength = len(myString)
myQuestion = myStringLength - 1
print(myString[myQuestion:])