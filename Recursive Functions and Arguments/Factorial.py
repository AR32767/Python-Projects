def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return "Invalid number."
    else:
        return num*factorial(num-1)

num = int(input("Enter a number to get the factorial of here... "))
print(factorial(num))