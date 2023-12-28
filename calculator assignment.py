operation=input("For addition operation press 1 \nFor subtraction operation press 2\nFor multiplication operation press 3 \nFor division operation press 4\nTo exit press any other key")
if operation=="1":
    number1,number2=eval(input("Enter the two numbers to be added seperated by comma"))
    sum=number1+number2
    print("the sum of the two numbers is",sum)
    decision=input("\nTo repeat the operation press 1 \n Press any other key to go to main menu")
    if decision=="1":
        number1,number2=eval(input("Enter the two numbers to be added seperated by comma"))
        sum=number1+number2
        print("the sum of the two numbers is",sum)
    else:
        operation=input("For addition operation press 1 \nFor subtraction operation press 2\nFor multiplication operation press 3 \nFor division operation press 4\nTo exit press any other key")
elif operation=="2":
    number1,number2=eval(input("Enter the two numbers to be subtracted seperated by comma"))
    subtraction=number1-number2
    print("the subtraction of the two numbers is",subtraction)
    decision=input("\nTo repeat the operation press 1 \n Press any other key to go to main menu")
    if decision=="1":
        number1,number2=eval(input("Enter the two numbers to be subtracted seperated by comma"))
        subtraction=number1+number2
        print("the subtraction of the two numbers is",subtraction)
    else:
        operation=input("For addition operation press 1 \nFor subtraction operation press 2\nFor multiplication operation press 3 \nFor division operation press 4\nTo exit press any other key")
elif operation=="3":
    number1,number2=eval(input("Enter the two numbers to be multiplied seperated by comma"))
    multiplication=number1*number2
    print("the product of the two numbers is",multiplication)
    decision=input("\nTo repeat the operation press 1 \n Press any other key to go to main menu")
    if decision=="1":
        number1,number2=eval(input("Enter the two numbers to be multiplied seperated by comma"))
        multiplication=number1*number2
        print("the product of the two numbers is",multiplication)
    else:
        operation=input("For addition operation press 1 \nFor subtraction operation press 2\nFor multiplication operation press 3 \nFor division operation press 4\nTo exit press any other key")
elif operation=="4":
    number1,number2=eval(input("Enter the two numbers to be divided seperated by comma"))
    divide=number1/number2
    print("the quotient of the two numbers is",divide)
    decision=input("\nTo repeat the operation press 1 \n Press any other key to go to main menu")
    if decision=="1":
        number1,number2=eval(input("Enter the two numbers to be divided seperated by comma"))
        divide=number1/number2
        print("the quotient of the two numbers is",divide)
    else:
        operation=input("For addition operation press 1 \nFor subtraction operation press 2\nFor multiplication operation press 3 \nFor division operation press 4\nTo exit press any other key")
else:
    print("exited")

