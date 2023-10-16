MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# TODO 4. Check if resources are sufficient?
def check_resources(order_ingredients):
    """Return's T/F is there is enough ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"There is not enough {item}.")
            return False
        return True


# TODO 5. process coins
def process_coins():
    """Return's the total calculation of coins added in"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * .01
    return total


# TODO 6. Check transaction successful
def transaction_success(payment_received, order_cost):
    """Return T if payment is accepted"""
    if payment_received >= order_cost:
        change = round(payment_received - order_cost, 2)
        global profit
        profit += order_cost
        print("Thanks")
        if change > 0:
            print(f"Here is your change ${change}")
        return True
    elif payment_received < order_cost:
        print(f"Sorry that's not enough money, the cost is {order_cost}. Money refunded {payment_received}")
        return False


# TODO 7. Make Coffee
def make_coffee(drink_name, order_ingredients):
    """ Deduct required ingredients"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy! 😄")


# TODO 1. Prompt user by asking what would you like? espresso/latte/cappuccino
def coffee_machine():
    run_machine = True
    while run_machine:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        # TODO 2.turn off the coffee machine by entering "off" to the prompt
        if order == "off":
            run_machine = False

        # TODO 3. Print report
        elif order == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[order]
            if check_resources(drink['ingredients']):
                payment = process_coins()
                if transaction_success(payment, drink['cost']):
                    make_coffee(order, drink['ingredients'])


coffee_machine()
