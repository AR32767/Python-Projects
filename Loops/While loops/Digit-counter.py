num = int(input("Enter a number here... "))
i = 0
while num >= 10:
    i = i + 1
    num = num//10
print(i,"is the number of digits in inputted number.")
