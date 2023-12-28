import random
def sum(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    if num2==0:
        num2=num2+1
    return num1/num2

def main():
    choice=input("Welcome to the maths quiz\nPress 1 for addition\nPress 2 for subtraction\nPress 3 for division")
    while choice!="1" and choice!="3" and choice!="2":
        choice=input("Welcome to the maths quiz\nPress 1 for addition\nPress 2 for subtraction\nPress 3 for division")
    choice=int(choice)
    repeat="y"
    marks=0
    count=0
    while repeat=="y":
        num1=random.randint(1,10)
        num2=random.randint(1,10)
        if choice==1:
            print(num1,"+",num2,"= ",end="")
            answer=int(input())
            result=sum(num1,num2)
            if answer==result:
                marks=marks+1
        elif choice==2:
            print(num1,"-",num2,"= ",end="")
            answer=int(input())
            result=sub(num1,num2)
            if answer==result:
                marks=marks+1
        elif choice==3:
            print(num1,"/",num2,"= ",end="")
            answer=float(input())
            result=div(num1,num2)
            result=round(result,2)
            if answer==result:
                marks=marks+1
        count=count+1
        repeat=input("Press y to try again or any other key to exit")
        if repeat=="y":
            choice=int(input("\nPress 1 for addition\nPress 2 for subtraction\nPress 3 for division"))
    print("you got",marks,"out of",count)
main()