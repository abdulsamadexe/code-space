menu = {
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
        "cost":2.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
earning=0
while True:
    order=input("What would you like? (espresso/latte/cappuchino) : ")
    
    a=0
    if order=="report":
            print("water :",resources['water'])
            print("milk :",resources['milk'])
            print("coffee :",resources['coffee'])
    elif order=="espresso":
        if resources["water"]>menu["espresso"]["ingredients"]["water"] and resources["coffee"]>menu["espresso"]["ingredients"]["coffee"]:
            print("please insert coins")
            quarters=int(input("How many quarters? "))
            dimes=int(input("What many dimes? "))
            pennies=int(input("how many pennies? "))
            nickles=int(input("How many nickles? "))
            amount= quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
            resources["water"]-=menu["espresso"]["ingredients"]["water"]
            resources["coffee"]-=menu["espresso"]["ingredients"]["coffee"]
            change=amount-menu['espresso']['cost']
            earning+=menu['espresso']['cost']
            print(f"Here is your ${change} change")
            print("Here is your espresso . Enjoy")
        else:
            print("Sorry,there are not enough resources for your order")


    elif order=="latte":
        if resources["water"]>menu["latte"]["ingredients"]['water'] and resources['milk']>menu["latte"]["ingredients"]['milk'] and resources['coffee']>menu["latte"]["ingredients"]['coffee']:
                print("please insert coins")
                quarters=int(input("How many quarters? "))
                dimes=int(input("What many dimes? "))
                pennies=int(input("how many pennies? "))
                nickles=int(input("How many nickles? "))
                amount= quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
                resources["water"]-=menu["latte"]["ingredients"]["water"]
                resources["coffee"]-=menu["latte"]["ingredients"]["coffee"]
                change=amount-menu['latte']['cost']
                resources["milk"]-=menu["latte"]["ingredients"]["milk"]
                earning+=menu['latte']['cost']
                print(f"Here is your ${change} change")
                print("Here is your latte . Enjoy")
        else:
            print("Sorry,there are not enough resources for your order")
    elif order=='cappuccino':
        if resources["water"]>menu["cappuccino"]["ingredients"]['water'] and resources['milk']>menu["cappuccino"]["ingredients"]['milk'] and resources['coffee']>menu["cappuccino"]["ingredients"]['coffee']:
                print("please insert coins")
                quarters=int(input("How many quarters? "))
                dimes=int(input("What many dimes? "))
                pennies=int(input("how many pennies? "))
                nickles=int(input("How many nickles? "))
                amount= quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
                resources["water"]-=menu["cappuccino"]["ingredients"]["water"]
                resources["coffee"]-=menu["cappuccino"]["ingredients"]["coffee"]
                change=amount-menu['cappuccino']['cost']
                resources["milk"]-=menu["cappuccino"]["ingredients"]["milk"]
                earning+=menu['cappuccino']['cost']
                print(f"Here is your ${change} change")
                print("Here is your cappuccino . Enjoy")

        else:
            print("Sorry,there are not enough resources for your order")
        
