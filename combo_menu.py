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
        drink_choice = fries_choice() # CALL FRIES CHOICE AND STORE RETURNED PRICE #
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
        print("Moving on to Fries...") # MOVING ON MESSAGE #
        fries_choice(price, drink_price) # CALL FRIES CHOICE WITH SANDWICH AND DRINK PRICES #
        return # RETURN AFTER ALL CHOICES COMPLETE #
    elif confirm.lower() == "no": # CHECK IF USER DENIED #
        print("Restarting Sandwich Selection...") # RESTART MESSAGE #
        return sandwich_choice() # RESTART FUNCTION AND RETURN RESULT #

def fries_choice(sandwich_price, drink_price): # FRIES CHOICE FUNCTION, ACCEPTS PREVIOUS PRICES #
    print("Please Choose a Fries Option:") # FRIES OPTIONS HEADER #
    print("Here are the Options") # OPTIONS HEADER #
    print("1. Small") # SMALL FRIES OPTION #
    print("2. Medium") # MEDIUM FRIES OPTION #
    print("3. Large") # LARGE FRIES OPTION #
    fries_option = input("Enter the number of your choice: ") # USER INPUT #
    fries_prices = {"Small": small_fries, "Medium": medium_fries, "Large": large_fries} # FRIES PRICES DICTIONARY #
    if fries_option == "1": # CHECK IF SMALL SELECTED #
        confirm = input("You've Selected Small, Are you Sure? (Yes/No): ") # CONFIRM SMALL SELECTION #
        choice = "Small" # STORE SMALL CHOICE #
    elif fries_option == "2": # CHECK IF MEDIUM SELECTED #
        confirm = input("You've Selected Medium, Are you Sure? (Yes/No): ") # CONFIRM MEDIUM SELECTION #
        choice = "Medium" # STORE MEDIUM CHOICE #
    elif fries_option == "3": # CHECK IF LARGE SELECTED #
        confirm = input("You've Selected Large, Are you Sure? (Yes/No): ") # CONFIRM LARGE SELECTION #
        choice = "Large" # STORE LARGE CHOICE #
    else: # IF INVALID OPTION #
        print("Invalid option, Please try again") # INVALID OPTION MESSAGE #
        return fries_choice(sandwich_price, drink_price) # RESTART FUNCTION AND RETURN RESULT #
    if confirm.lower() == "yes": # CHECK IF USER CONFIRMED #
        price = fries_prices[choice] # GET PRICE FROM DICTIONARY #
        print(f"You have Ordered {choice} Fries!") # PRINT THEIR CHOICE #
        if fries_option == "1": # CHECK IF SMALL SELECTED #
            print("You have Ordered Small Fries, Would you like to supersize your Fries? (Yes/No): ") # SUPERSIZE OPTION #
            supersize_option = input() # USER INPUT #
            if supersize_option.lower() == "yes": # CHECK IF USER WANTS TO SUPERSIZE #
                price = large_fries # UPDATE PRICE TO LARGE #
                print("Your Fries have been Supersized to Large!") # SUPERSIZE CONFIRM #
                print("#------------------------------#") # DIVIDER #
                total = sandwich_price + drink_price + price # RECALCULATE TOTAL COST #
                print(f"Sandwich Cost: ${sandwich_price:.2f}") # PRINT SANDWICH COST #
                print(f"Drink Cost: ${drink_price:.2f}") # PRINT DRINK COST #
                print(f"Fries Cost: ${price:.2f}") # PRINT UPDATED FRIES COST #
                print(f"Total Cost: ${total:.2f}") # PRINT UPDATED TOTAL COST #
                return total # RETURN UPDATED TOTAL COST #
            elif supersize_option.lower() == "no": # CHECK IF USER DOES NOT WANT TO SUPERSIZE #
                print("Your Fries will remain Small.") # NO SUPERSIZE CONFIRM #
                print("#------------------------------#") # DIVIDER #
                total = sandwich_price + drink_price + price # CALCULATE TOTAL COST #
                print(f"Sandwich Cost: ${sandwich_price:.2f}") # PRINT SANDWICH COST #
                print(f"Drink Cost: ${drink_price:.2f}") # PRINT DRINK COST #
                print(f"Fries Cost: ${price:.2f}") # PRINT FRIES COST #
                print(f"Total Cost: ${total:.2f}") # PRINT TOTAL COST #
                return total # RETURN TOTAL COST #
        print(f"Fries Cost: ${price:.2f}") # PRINT FRIES COST #
        print("#------------------------------#") # DIVIDER #
        total = sandwich_price + drink_price + price # CALCULATE TOTAL COST #
        print(f"Sandwich Cost: ${sandwich_price:.2f}") # PRINT SANDWICH COST #
        print(f"Drink Cost: ${drink_price:.2f}") # PRINT DRINK COST #
        print(f"Fries Cost: ${price:.2f}") # PRINT FRIES COST #
        print(f"Total Cost: ${total:.2f}") # PRINT TOTAL COST #
        return total # RETURN TOTAL COST #
    elif confirm.lower() == "no": # CHECK IF USER DENIED #
        print("Restarting Fries Selection...") # RESTART MESSAGE #
        return fries_choice(sandwich_price, drink_price) # RESTART FUNCTION AND RETURN RESULT #

print("#------------------------------#") # DIVIDER #
sandwich_choice() # CALL SANDWICH CHOICE FUNCTION # ## END OF NOW 02/18 ###
print("#------------------------------#") # DIVIDER #