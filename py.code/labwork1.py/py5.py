# Sample list containing 'Red' at index 3
colors = ["black", "blue", "yellow", "Red", "white"] 

user_color = input("Whatt is your fvourite colour? ")

if user_color in colors:
    index = colors.index(user_color)
    print(f"Your color is at index {index} in my list")
else:
    print(f"Sorry, I could not find your color" )