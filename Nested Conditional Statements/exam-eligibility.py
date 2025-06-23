# Write a program to check whether the student can take an
# exam or not. Students will be allowed only in two conditions: 
#If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance 
# If attendance is above 75, then allowed; otherwise, not allowed.

print("If you have had a medical issue, type 'Yes'. Otherwise, type 'No.'")
medical = input("Enter Yes or No here: ")
attendance = float(input("Enter the percentage of students attending the exam here: "))

if medical.lower() == "yes":
    print("You are eligible to enter the exam.")
else:
    if attendance > float(75):
        print("You are eligible to attend the exam.")
    else:
        print("You are not eligible to attend the exam")