import time # IMPORT TIME MODULE FOR DELAYS #


# CMD SANDWICH SHOP #
print("Welcome to CMD Sandwich Shop!") # WELCOME MESSAGE #
print("Here are our combo meals:") # COMBO MEALS HEADER #

chicken = 5.25      # PRICE OF CHICKEN SANDWICH #
beef = 6.25         # PRICE OF BEEF SANDWICH #
tofu = 5.75         # PRICE OF TOFU SANDWICH #
small_drink = 1.00  # PRICE OF SMALL DRINK #
medium_drink = 1.75 # PRICE OF MEDIUM DRINK #
large_drink = 2.25  # PRICE OF LARGE DRINK #
small_fries = 1.00  # PRICE OF SMALL FRIES #
medium_fries = 1.50 # PRICE OF MEDIUM FRIES #
large_fries = 2.00  # PRICE OF LARGE FRIES #
ketchup_packet = 0.25 # PRICE OF KETCHUP PACKET #

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
    if confirm.lower() in ("yes", "y"): # CHECK IF USER CONFIRMED #
        price = drink_prices[choice] # GET PRICE FROM DICTIONARY #
        print(f"You have Ordered a {choice} Drink!") # PRINT THEIR CHOICE #
        print(f"Drink Cost: ${price:.2f}") # PRINT DRINK COST #
        return price # RETURN DRINK PRICE #
    elif confirm.lower() in ("no", "n"): # CHECK IF USER DENIED #
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
    if confirm.lower() in ("yes", "y"): # CHECK IF USER CONFIRMED #
        price = sandwich_prices[choice] # GET PRICE FROM DICTIONARY #
        print(f"You have Ordered a {choice} Sandwich!") # PRINT THEIR CHOICE #
        print(f"Sandwich Cost: ${price:.2f}") # PRINT SANDWICH COST #
        print("#------------------------------#") # DIVIDER #
        print(f"Total so far: ${price:.2f}") # PRINT RUNNING TOTAL #
        print("#------------------------------#") # DIVIDER #
        print("Moving on to Drinks...") # MOVING ON MESSAGE #
        drink_price = drink_choice() # CALL DRINK CHOICE AND STORE RETURNED PRICE #
        print("#------------------------------#") # DIVIDER #
        print(f"Total so far: ${price + drink_price:.2f}") # PRINT RUNNING TOTAL AFTER DRINK #
        print("#------------------------------#") # DIVIDER #
        print("Moving on to Fries...") # MOVING ON MESSAGE #
        fries_choice(price, drink_price) # CALL FRIES CHOICE WITH SANDWICH AND DRINK PRICES #
        return # RETURN AFTER ALL CHOICES COMPLETE #
    elif confirm.lower() in ("no", "n"): # CHECK IF USER DENIED #
        print("Restarting Sandwich Selection...") # RESTART MESSAGE #
        return sandwich_choice() # RESTART FUNCTION AND RETURN RESULT #

def fries_choice(sandwich_price, drink_price): # FRIES CHOICE FUNCTION #
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
        return fries_choice(sandwich_price, drink_price) # RESTART FUNCTION #
    if confirm.lower() in ("yes", "y"): # CHECK IF USER CONFIRMED #
        price = fries_prices[choice] # GET PRICE FROM DICTIONARY #
        print(f"You have Ordered {choice} Fries!") # PRINT THEIR CHOICE #
        if fries_option == "1": # CHECK IF SMALL SELECTED FOR SUPERSIZE #
            supersize_option = input("Would you like to Supersize your Fries to Large? (Yes/No): ") # SUPERSIZE OPTION #
            if supersize_option.lower() in ("yes", "y"): # CHECK IF USER WANTS TO SUPERSIZE #
                price = large_fries # UPDATE PRICE TO LARGE #
                print("Your Fries have been Supersized to Large!") # SUPERSIZE CONFIRM #
        print(f"Fries Cost: ${price:.2f}") # PRINT FRIES COST #
        total = sandwich_price + drink_price + price # CALCULATE TOTAL BEFORE DISCOUNT #
        combo_discount = 0 # DEFAULT COMBO DISCOUNT TO 0 #
        if sandwich_price and drink_price and price: # CHECK IF ALL THREE ITEMS ORDERED #
            combo_discount = 1.00 # SET COMBO DISCOUNT TO $1.00 #
            total = total - combo_discount # APPLY COMBO DISCOUNT TO TOTAL #
            print("Combo Discount Applied! You Saved $1.00!") # COMBO DISCOUNT MESSAGE #
        print("#------------------------------#") # DIVIDER #
        print(f"Total so far: ${total:.2f}") # PRINT RUNNING TOTAL AFTER FRIES #
        print("#------------------------------#") # DIVIDER #
        print("Moving on to Sauce Packets...") # MOVING ON MESSAGE #
        packets_total = packets_choice(total, sandwich_price, drink_price, price, combo_discount) # CALL PACKETS CHOICE #
        return packets_total # RETURN FINAL TOTAL #
    elif confirm.lower() in ("no", "n"): # CHECK IF USER DENIED #
        print("Restarting Fries Selection...") # RESTART MESSAGE #
        return fries_choice(sandwich_price, drink_price) # RESTART FUNCTION #

def packets_choice(total, sandwich_price, drink_price, fries_price, combo_discount): # SAUCE PACKETS CHOICE FUNCTION #
    print("#------------------------------#") # DIVIDER #
    sauce_option = input("Would you like to add Sauce Packets to your order? (Yes/No): ") # USER INPUT #
    if sauce_option.lower() in ("yes", "y"): # CHECK IF USER WANTS SAUCE PACKETS #
        print("How many Ketchup Packets would you like to add? (1-100): ") # NUMBER OF PACKETS OPTION #
        while True: # LOOP UNTIL VALID INPUT #
            try: # TRY TO CONVERT INPUT TO INTEGER #
                num_packets = int(input()) # USER INPUT #
                if 1 <= num_packets <= 100: # CHECK IF NUMBER IS BETWEEN 1 AND 100 #
                    ketchup_cost = ketchup_packet * num_packets # CALCULATE KETCHUP COST #
                    new_total = total + ketchup_cost # ADD KETCHUP COST TO TOTAL #
                    print(f"{num_packets} Ketchup Packets have been added to your order!") # CONFIRMATION #
                    print(f"Ketchup Packets Cost: ${ketchup_cost:.2f}") # PRINT KETCHUP COST #
                    print("#------------------------------#") # DIVIDER #
                    print(f"Sandwich Cost:        ${sandwich_price:.2f}") # PRINT SANDWICH COST #
                    print(f"Drink Cost:           ${drink_price:.2f}") # PRINT DRINK COST #
                    print(f"Fries Cost:           ${fries_price:.2f}") # PRINT FRIES COST #
                    print(f"Ketchup Packets Cost: ${ketchup_cost:.2f}") # PRINT KETCHUP COST #
                    if combo_discount > 0: # CHECK IF COMBO DISCOUNT APPLIED #
                        print(f"Combo Discount:       -${combo_discount:.2f}") # PRINT COMBO DISCOUNT #
                    print("#------------------------------#") # DIVIDER #
                    print(f"Total Cost:           ${new_total:.2f}") # PRINT FINAL TOTAL #
                    return new_total # RETURN UPDATED TOTAL #
                else: # IF NUMBER OUT OF RANGE #
                    print("Invalid number, Please enter a number between 1 and 100: ") # INVALID NUMBER #
            except ValueError: # IF INPUT IS NOT A NUMBER #
                print("Invalid input, Please enter a valid number: ") # INVALID INPUT MESSAGE #
    elif sauce_option.lower() in ("no", "n"): # CHECK IF USER DOES NOT WANT SAUCE PACKETS #
        print("No Sauce Packets will be added to your order.") # NO SAUCE PACKETS CONFIRMATION #
        print("#------------------------------#") # DIVIDER #
        print(f"Sandwich Cost: ${sandwich_price:.2f}") # PRINT SANDWICH COST #
        print(f"Drink Cost:    ${drink_price:.2f}") # PRINT DRINK COST #
        print(f"Fries Cost:    ${fries_price:.2f}") # PRINT FRIES COST #
        if combo_discount > 0: # CHECK IF COMBO DISCOUNT APPLIED #
            print(f"Combo Discount: -${combo_discount:.2f}") # PRINT COMBO DISCOUNT #
        print("#------------------------------#") # DIVIDER #
        print(f"Total Cost:    ${total:.2f}") # PRINT TOTAL #
        return total # RETURN UNCHANGED TOTAL #
    else: # IF INVALID OPTION #
        print("Invalid option, Please try again") # INVALID OPTION MESSAGE #
        return packets_choice(total, sandwich_price, drink_price, fries_price, combo_discount) # RESTART FUNCTION #

print("#------------------------------#") # DIVIDER #
sandwich_choice() # CALL SANDWICH CHOICE FUNCTION #
print("#------------------------------#") # DIVIDER #
print("Thank you for ordering at CMD Sandwich Shop! Your order will be ready shortly.") # THANK YOU MESSAGE #

time.sleep(5) # WAIT 5 SECONDS BEFORE ENDING PROGRAM #
print("Your order is ready! Please pick it up at the counter. Have a great day!") # ORDER READY MESSAGE #