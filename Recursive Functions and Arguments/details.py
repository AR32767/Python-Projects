def id(num):
    if num == 1:
        return "name: John \n department: Sales \n salary: 100k - 200k per 6 months \n id: 1"
    elif num == 2:
        return "name: Saily \n department: A and M \n salary: 150k - 300k per 12 months \n id: 2"
    elif num == 3:
        return "name: Andrew \n department: Executive \n salary: 300-500k per 6 months \n id: 3"
    else:
        return "Invalid ID. Please try again and enter a valid ID."    
    
uid = int(input("Enter an ID here... "))

print(id(uid))