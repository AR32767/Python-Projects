num = int(input("Enter a number here... "))
temp = num
count = 0
while temp > 0:
    count += 1
    temp //=10
if count %2 == 0:
    mid = count//2
    mid2 = mid+1
    temp = num
    pos = 0
    while temp > 10**(count-2):
        digit = temp % 10
        if pos == mid:
            mid = digit
        elif pos == mid2:
            mid2 = digit
        temp//=10
        pos +=1
    product = mid*mid2
    print(product)