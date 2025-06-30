import math
num1 = float(input("Enter the base number here... "))
num2 = int(input("Enter the exponent you want to raise the number to here. "))
# print(math.pow(num1,num2)) #Alternative option
# print(num1**num2) # Check if correct
temp = num1
for i in range (1,num2):
    num1 *= temp
print(num1, "\n")


