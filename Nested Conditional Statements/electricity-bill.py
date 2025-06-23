units = int(input("Enter the # of units of electricity consumed. "))

if units <= 50:
    total = (units*2.60)+25
    print("The cost is: ", total, " rupees, including tax.")
elif units >50 and units <= 100:
    total = (130 + (units-50)*3.25)+35
    print("The cost is: ", total, " rupees, including tax")
elif units > 100 and units <= 200:
    total = (292.5 + (units-100)*5.26)+45
    print("The cost is: ", total," rupees, including tax")
else:
    total = (818.5+(units-200)*8.45)+75
    print("The cost is: ", total," rupees, including tax")