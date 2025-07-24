def tip_paid(total, tip):
    tip_amount = total*(tip/100)
    return tip_amount

total = float(input("Enter the total amount paid here... "))
percent_tipped = float(input("Enter the amount tipped here... "))
print(f"The tip paid is ${tip_paid(total, percent_tipped)}. \n")

print(f"The total is ${total+tip_paid(total,percent_tipped)}.")