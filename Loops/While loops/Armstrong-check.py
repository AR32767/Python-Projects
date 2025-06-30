num = int(input("Enter a number here... "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10

if num == sum:
    print("Your number is an Armstrong number.")
else:
    print("Your number is not an Armstrong number.")