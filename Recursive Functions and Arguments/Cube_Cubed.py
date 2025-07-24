def cube(num):
    return num**3
def c_cube(num):
    if num % 3 == 0:
        return cube(num)
    else: return num

num = float(input("Enter a number here... "))

print(c_cube(num))