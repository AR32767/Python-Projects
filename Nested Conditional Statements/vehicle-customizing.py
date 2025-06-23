print("Enter a catagory and subcatagory to customize your favorite car here!")
cls = input("Do you prefer cars or bikes? (Enter here...) ")
if cls == "cars":
    subcls = input("Is the car an SUV or a sedan? ")
    if subcls == "SUV":
        print("Enjoy your SUV car ride!")
    elif subcls == "sedan":
        print("Enjoy your sedan ride!")
    else:
        print("Invalid input. Please try again.")
elif cls == "bike":
    subcls = input("Is the bike motorized or pedal-powered? ")
    if subcls == "motorized":
        print("Enjoy your motorcycle!")
    elif subcls ==  "pedal-powered":
        print("Enjoy your bicycle!")
    else:
        print("Invalid input. Please try again.")
else:
    print("Invalid input. Please try again.")