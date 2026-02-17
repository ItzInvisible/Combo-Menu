print("Welcome to CMD Sandwich Shop!")
print("Here are our combo meals:")
# print("1. Classic Combo: Sandwich, Fries, and a Drink")

# Mention Variable of the person of user
chicken = 5.25, 
beef = 6.25,
tofu = 5.75,
small_drink = 1.00,
medium_drink = 1.75,
large_drink = 2.25,

# Ask for Sandwich Choice
def sandwich_choice():
    input("Please Choose a Sandwich Option:") # SANDWICH OPTIONS #
    print("Here are the Options") # SANDWICH OPTIONS #
    print("1. Chicken") # CHICKEN OPTION SELECTION #
    print("2. Beef") # BEEF OPTION SELECTION #
    print("3. Tofu") # TOFU OPTION SELECTION #
    sandwich_option = input("Enter the number of your choice: ") # CHICKEN OPTION SELECTION #
    if sandwich_option == "1": # CHICKEN OPTION SELECTION #
        return input("You've Selected Chicken Are you Sure?") # CHICKEN OPTION SELECTION #
    elif sandwich_option == "2": # BEEF OPTION SELECTION #
        return input("You've Selected Beef Are you Sure?") # BEEF OPTION SELECTION #
    elif sandwich_option == "3": # TOFU OPTION SELECTION #
        return input("You've Selected Tofu Are you Sure?") # TOFU OPTION SELECTION #

print("#------------------------------#") # SANDWICH CHOICES START #
print(sandwich_choice())
print("#------------------------------#") # SANDWICH CHOICES END #


print("Press the number of the Sandwich to Confirm your Order")

if sandwich_option == 1:           # ← no leading indent
    print("You have Confirmed Chicken")  # ← indented inside the if
elif sandwich_option == 2:
    print("You have Confirmed Beef")
elif sandwich_option == 3:
    print("You have Confirmed Tofu")