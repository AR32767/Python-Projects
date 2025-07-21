season = input("Enter 'spring' or 'autumm' here... ")
def weather_condition(season):
    if season == "spring":
        print("Spring is generally warm. Lighter clothes and rainjackets are recommended.")
    elif season == "autumm":
        print("Autumm (or fall) is usually cool. I would reccommend wearing moderate clothing.")
    else:
        print("Invalid answer. Please run the program and try again.")

weather_condition(season)