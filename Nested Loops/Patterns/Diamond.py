maxRows = int(input("Enter the maximum number of rows to generate here. "))
if maxRows % 2 ==0:
    mid = maxRows//2
else:
    mid = maxRows//2+1
space = mid-1
for i in range(1,mid+1):
    counter = 1
    for j in range(space):
        print(" ",end="")
    space= space-1
    for j in range(2*i-1):
        print(counter,end="")
        counter +=1
    print()
space = 1
for i in range(1, mid+1):
    for j in range(space):
        print(" ",end="")
    space +=1
    counter = 1
    for j in range(2*(mid-i)-1):
        print(counter,end="")
        counter += 1
    print()

