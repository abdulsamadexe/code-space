# import random
# count=0
# score=0
# while count<5:
#     count=count+1
#     num1=random.randint(0,9)
#     num2=random.randint(0,9)
#     operations=["+","-","*","/"]
#     op=random.choice(operations)
#     if op=="+":
#         sum=num1+num2
#         print(num1,op,num2,"=",end="")
#         answer=int(input(""))
#         if answer==sum:
#             score=score+1
#     elif op=="-":
#         diff=num1-num2
#         print(num1,op,num2,"=",end="")
#         answer=int(input(""))
#         if answer==diff:
#             score=score+1
#     elif op=="*":
#         product=num1*num2
#         print(num1,op,num2,"=",end="")
#         answer=int(input(""))
#         if answer==product:
#             score=score+1
#     elif op=="/":
#         if num2==0:
#             num2=num2+random.randint(1,9)
#             quotient=num1/num2
#             print(num1,op,num2,"=",end="")
#             answer=float(input("Enter the asnwer upto 2 decimal places"))
#             answer=round(answer,2)
#             if answer==quotient:
#                 score=score+1
#         else:
#             quotient=num1/num2
#             print(num1,op,num2,"=",end="")
#             answer=float(input("Enter the asnwer upto 2 decimal places"))
#             answer=round(answer,2)
#             if answer==quotient:
#                 score=score+1
# print("your score is",score,"out of 5")
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
    choice=int(input("Welcome to the maths quiz\nPress 1 for addition\nPress 2 for subtraction\nPress 3 for division"))
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
