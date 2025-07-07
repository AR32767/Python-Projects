maxRows = int(input("Enter the maximum number of rows to generate here. "))
counter = 1
for i in range(1,maxRows+1):
    for j in range(1,i+1):
        print(counter,end=" ")
        counter += 1
    print()