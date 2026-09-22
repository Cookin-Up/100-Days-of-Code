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

coffee_machine = True
current_resources = resources
profit = 0

#TODO: 7) Make coffee and use resources
def make_coffee():
        print(f"Here is your {drink_selection}")
        for ingredient in MENU[drink_selection]["ingredients"]:
            current_resources[ingredient] -= MENU[drink_selection]["ingredients"][ingredient]
        change = total - MENU[drink_selection]["cost"]
        change = round(change, 2)
        print(f"Change is {change}")
        global  profit
        profit += MENU[drink_selection]["cost"]
        profit = round(profit, 2)

def check_resources(selection):
    for ingredient in MENU[selection]["ingredients"]:
        if MENU[selection]["ingredients"][ingredient] > current_resources[ingredient]:
            print(f"Not enough {ingredient}")
            return False
    return True

def calc_coins(q, d, n, p):
    total = 0
    total += q * .25
    total += d * .1
    total += n * .05
    total += p * .01
    total = round(total, 2)
    print(f"You have {total}")
    return total

    # TODO: 6) Check transaction successful? Refund if too little, or if Y move to 7

def check_trans():
    total = calc_coins(quarters, dimes, nickles, pennies)
    if total >= MENU[drink_selection]["cost"]:
        print("Making drink...")
        return total

    elif total < MENU[drink_selection]["cost"]:
        print("Not enough money, refunding")
#TODO: 1)  Prompt user by asking “What would you like? (espresso/latte/cappuccino): "

#TODO: 2)  Turn off the Coffee Machine by entering “off" to the prompt.


while coffee_machine == True:
    drink_selection = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if drink_selection == "off":
        print("Goodbye")
        break

    # TODO: 3) Print a report of all coffee machine resources
    if drink_selection == "report":
        print(
            f'Water left: {current_resources["water"]}, Milk left: {current_resources["milk"]}, Coffee left: {current_resources["coffee"]}, Profit made: {round(profit, 2)}')
        continue
    if check_resources(drink_selection) == False:
        continue
    #TODO: 5) Process coins
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    total = check_trans()
    if total is None:
        continue

    make_coffee()

