from data import MENU, resources

money = 0
working = True
while working:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("Good Bye!")
        working = False

    elif user_choice == "report":
        print(f'''
water = {resources["water"]}
milk = {resources["milk"]}
coffee = {resources["coffee"]}
money = {money}
    ''')

    elif user_choice != "espresso" and user_choice != "latte" and user_choice != "cappuccino":
        print("Please type a valid command.")

    else:
        coffee = user_choice
        for ingredient in MENU[coffee]["ingredients"]:

            if MENU[coffee]["ingredients"][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.\n")
                break
            else:
                print(f"\nThe {coffee} is ${MENU[coffee]['cost']} please insert coins.\n")
                quarter_input = int(input("quarter count: "))
                dime_input = int(input("dime count: "))
                nickle_input = int(input("nickle count: "))
                penny_input = int(input("penny count: "))
                total_money_input = quarter_input*0.25 + dime_input*0.10 + nickle_input*0.05 + penny_input*0.01

                if total_money_input >= MENU[coffee]['cost']:
                    change = total_money_input - MENU[coffee]['cost']
                    money += MENU[coffee]['cost']
                    for ingredients in MENU[coffee]["ingredients"]:
                        resources[ingredients] -= MENU[coffee]["ingredients"][ingredients]

                    if change > 0:
                        print(f'\nHere is your change: ${"{:.2f}".format(change)}')
                        print(f"Enjoy your {coffee}!!!\n")
                    else:
                        print(f"Enjoy your {coffee}!!!\n")

                else:
                    print('Sorry that\'s not enough money. Money refunded.\n')

                break
