options = ["boy", "girl", "cat", "dog"]

def get_index(user_choice):    
    if user_choice not in options:
        return "Not available. Try again."
    option_index = options.index(user_choice)
    return f"Your choice is ranked: {option_index}"

def breakdown(user_choice):
    for x in user_choice:
        print(x)

while True:
    user_choice = input("Enter an option: ").lower()
    result = get_index(user_choice)
    
    if "Not available" in result:
        print(result)
        continue
    else:
        print(result)
        breakdown(user_choice)
        break

