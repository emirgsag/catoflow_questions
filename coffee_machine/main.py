from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

is_working = True
while is_working:
    choice = input(f"What would you like{menu.get_items()}? ")

    if choice == "report":
        machine.report()
        money_machine.report()

    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        choice = menu.find_drink(choice)
        if machine.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                machine.make_coffee(choice)

    elif choice == "off":
        print("Good bye.")
        is_working = False

    else:
        print("Please choose a valid option.")
