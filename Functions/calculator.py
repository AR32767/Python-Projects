def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def exponent(a,b):
    return a**b

print("----------------CALCULATOR----------------")
print("NOTE: all operations perform the second number on the first number, not the other way around. \n")
operation = int(input("Enter the operation to perform here. 1 is addition, 2 is subtratction, 3 is multiplication, 4 is division, and 5 is exponentiation. "))
num1 = float(input("Enter the first number here... "))
num2 = float(input("Enter the second number here... "))
if operation == 1:
    print(addition(num1,num2))
elif operation == 2:
    print(subtraction(num1,num2))
elif operation == 3:
    print(multiplication(num1,num2))
elif operation == 4:
    print(division(num1,num2))
elif operation == 5:
    print(exponent(num1,num2))
else:
    print("Invalid input. Please try again")