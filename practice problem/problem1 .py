#1.	Write a program that generates a quiz of 5 questions. For each question generate two integers between (1-99) and randomly prompts the user to enter the +, -, *, or / of these two integers. The program then prints "Correct" if the answer is correct, otherwise prints Wrong and also provides the correct answer. At the end program print the user score in the quiz, such as 3 out of 5.
import random
count=0
marks=0
while count<5:
    count=count+1
    num1=random.randint(1,99)
    num2=random.randint(1,99)
    operators="*","-","+","/"
    op=random.choice(operators)
    if op=="*":
        result=num1*num2
        print(num1,op,num2,"=",end="")
        answer=int(input())
        if answer==result:
            print("your answer is correct")
            marks=marks+1
        else:
            print("your answer is inorrect")
            print("correct answer is",result)
    elif op=="+":
        print(num1,op,num2,"=",end="")
        result=num1+num2
        answer=int(input())
        if answer==result:
            print("your answer is correct")
            marks=marks+1
        else:
            print("your answer is inorrect")
            print("correct answer is",result)
    elif op=="-":
        if num2>num1:
            print(num2,op,num1,"=",end="")
        else:
            print(num1,op,num2,"=",end="")
        result=num1-num2
        answer=int(input())
        if answer==result:
            print("your answer is correct")
            marks=marks+1
        else:
            print("your answer is inorrect")
            print("correct answer is",result)
    elif op=="/":
        print(num1,op,num2,"=",end="")
        result=num1/num2
        answer=float(input())
        result=round(result,2)
        if answer==result:
            print("your answer is correct")
            marks=marks+1
        else:
            print("your answer is inorrect")
            print("correct answer is",result)
print("you got ",marks,"out of 5")

