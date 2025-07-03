string = input("Enter a string here... ")
char = input("Enter the character to check for here...")
i = 0
c = 0
for i in string:
    if i == char:
        c += 1
print(f"There are {c} {char}'s in the string.")