# CMD SANDWICH SHOP #
print("Welcome to CMD Sandwich Shop!") # WELCOME MESSAGE #
print("Here are our combo meals:") # COMBO MEALS HEADER #

chicken = 5.25      # PRICE OF CHICKEN SANDWICH #
beef = 6.25         # PRICE OF BEEF SANDWICH #
tofu = 5.75         # PRICE OF TOFU SANDWICH #
small_drink = 1.00  # PRICE OF SMALL DRINK #
medium_drink = 1.75 # PRICE OF MEDIUM DRINK #
large_drink = 2.25  # PRICE OF LARGE DRINK #
small_fries = 1.00 # PRICE OF SMALL FRIES #
medium_fries = 1.50 # PRICE OF MEDIUM FRIES #
large_fries = 2.00 # PRICE OF LARGE FRIES #

def drink_choice(): # DRINK CHOICE FUNCTION #
    print("Please Choose a Drink Option:") # DRINK OPTIONS HEADER #
    print("Here are the Options") # OPTIONS HEADER #
    print("1. Small") # SMALL DRINK OPTION #
    print("2. Medium") # MEDIUM DRINK OPTION #
    print("3. Large") # LARGE DRINK OPTION #
    drink_option = input("Enter the number of your choice: ") # USER INPUT #
    drink_prices = {"Small": small_drink, "Medium": medium_drink, "Large": large_drink} # DRINK PRICES DICTIONARY #
    if drink_option == "1": # CHECK IF SMALL SELECTED #
        confirm = input("You've Selected Small, Are you Sure? (Yes/No): ") # CONFIRM SMALL SELECTION #
        choice = "Small" # STORE SMALL CHOICE #
    elif drink_option == "2": # CHECK IF MEDIUM SELECTED #
        confirm = input("You've Selected Medium, Are you Sure? (Yes/No): ") # CONFIRM MEDIUM SELECTION #
        choice = "Medium" # STORE MEDIUM CHOICE #
    elif drink_option == "3": # CHECK IF LARGE SELECTED #
        confirm = input("You've Selected Large, Are you Sure? (Yes/No): ") # CONFIRM LARGE SELECTION #
        choice = "Large" # STORE LARGE CHOICE #
    else: # IF INVALID OPTION #
        print("Invalid option, Please try again") # INVALID OPTION MESSAGE #
        return drink_choice() # RESTART FUNCTION AND RETURN RESULT #
    if confirm.lower() == "yes": # CHECK IF USER CONFIRMED #
        price = drink_prices[choice] # GET PRICE FROM DICTIONARY #
        print(f"You have Ordered a {choice} Drink!") # PRINT THEIR CHOICE #
        print(f"Moving on to Fries...") # MOVING ON MESSAGE #
        return price # RETURN DRINK PRICE #
    elif confirm.lower() == "no": # CHECK IF USER DENIED #
        print("Restarting Drink Selection...") # RESTART MESSAGE #
        return drink_choice() # RESTART FUNCTION AND RETURN RESULT #

def sandwich_choice(): # SANDWICH CHOICE FUNCTION #
    print("Please Choose a Sandwich Option:") # SANDWICH OPTIONS HEADER #
    print("Here are the Options") # OPTIONS HEADER #
    print("1. Chicken") # CHICKEN OPTION #
    print("2. Beef") # BEEF OPTION #
    print("3. Tofu") # TOFU OPTION #
    sandwich_option = input("Enter the number of your choice: ") # USER INPUT #
    sandwich_prices = {"Chicken": chicken, "Beef": beef, "Tofu": tofu} # SANDWICH PRICES DICTIONARY #
    if sandwich_option == "1": # CHECK IF CHICKEN SELECTED #
        confirm = input("You've Selected Chicken, Are you Sure? (Yes/No): ") # CONFIRM CHICKEN SELECTION #
        choice = "Chicken" # STORE CHICKEN CHOICE #
    elif sandwich_option == "2": # CHECK IF BEEF SELECTED #
        confirm = input("You've Selected Beef, Are you Sure? (Yes/No): ") # CONFIRM BEEF SELECTION #
        choice = "Beef" # STORE BEEF CHOICE #
    elif sandwich_option == "3": # CHECK IF TOFU SELECTED #
        confirm = input("You've Selected Tofu, Are you Sure? (Yes/No): ") # CONFIRM TOFU SELECTION #
        choice = "Tofu" # STORE TOFU CHOICE #
    else: # IF INVALID OPTION #
        print("Invalid option, Please try again") # INVALID OPTION MESSAGE #
        return sandwich_choice() # RESTART FUNCTION AND RETURN RESULT #
    if confirm.lower() == "yes": # CHECK IF USER CONFIRMED #
        price = sandwich_prices[choice] # GET PRICE FROM DICTIONARY #
        print(f"You have Ordered a {choice} Sandwich!") # PRINT THEIR CHOICE #
        print(f"Sandwich Cost: ${price:.2f}") # PRINT SANDWICH COST #
        print("Moving on to Drinks...") # MOVING ON MESSAGE #
        drink_price = drink_choice() # CALL DRINK CHOICE AND STORE RETURNED PRICE #
        total = price + drink_price # CALCULATE TOTAL COST #
        print(f"Sandwich Cost: ${price:.2f}") # PRINT SANDWICH COST #
        print(f"Drink Cost: ${drink_price:.2f}") # PRINT DRINK COST
        print(f"Your total cost so far is: ${total:.2f}") # PRINT TOTAL COST #
        return total # RETURN TOTAL COST #
    elif confirm.lower() == "no": # CHECK IF USER DENIED #
        print("Restarting Sandwich Selection...") # RESTART MESSAGE #
        return sandwich_choice() # RESTART FUNCTION AND RETURN RESULT #

def fries_choice(): # FRIES CHOICE FUNCTION #
    






print("#------------------------------#") # DIVIDER #
sandwich_choice() # CALL SANDWICH CHOICE FUNCTION # ## END OF NOW 02/18 ###
print("#------------------------------#") # DIVIDER #