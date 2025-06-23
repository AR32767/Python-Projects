#ASCII Value Converter

char = input("Enter a character here: ")
print(ord(char))

#Value Swapping
a = int(input("Enter first number here... "))
b = int(input("Enter second number here... "))
c = int(input("Enter third number here... "))

temp = a 
a = b
b = c
c = temp
print(f"Your new values are: {a}, {b}, and {c}")