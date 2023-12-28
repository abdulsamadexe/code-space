#task 1
#taking input
number=eval(input("enter a four digit number"))
#seperaing digit 1
digit_1=(number//1000)
#seperating the remainder
remainder_1=(number%1000)
#seperting digit 2
digit_2=(remainder_1//100)
#seperting remainder_2
remainder_2=remainder_1%100
#seperating digit 3
digit_3=remainder_2//10
#seperating digit 4
digit_4=remainder_2%10
#adding the four digits
sum=digit_1+digit_2+digit_3+digit_4
#displayng the sum of four digitof the entered number 
print("the sum of the four digits of the given number is ",sum,"\n")


#task 2
weight_in_pounds=eval(input("enter your weight in pounds"))

height_in_inches=eval(input("enter your height in inches"))
height_in_metres=height_in_inches*0.0254
#converting weight intoo kilograms
weight_in_kilograms=weight_in_pounds*0.45359237
BMI=(weight_in_kilograms)/(height_in_metres**2)
#Displaying output                      
print("your BMI is ",BMI, "\n")


#task 3
M=eval(input("enter the amount of water in kgs "))
initial_temperature=eval(input("enter the initial temperature"))
final_temperature=eval(input("enter the final temperature"))
Q=M*(initial_temperature-final_temperature)*4185
print(f"energy required is {Q}\n")

#task 4
minutes=eval(input("ENTER THE NUMBER OF MINUTES :"))
no_of_days=minutes/(60*24)
no_of_years=minutes/(60*24*365)
print(f"Number of days :{no_of_days} \n Number of years :{no_of_years}")