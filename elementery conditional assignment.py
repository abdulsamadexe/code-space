#3) GRADED LAB TASKS IN THE MID
#LAB TASK 1
name=input("what is your name ?")
print("hi",name)

#LAB TASK 2
number=int(input("Enter the number"))
print("The square of the number",number,"is",number*number)

#LAB TASK 3
base=int(input("Enter the lenght of base of the triangle:"))
height=int(input("Enter the lenght of height of the triangle:"))
area=(1/2)*base*height
print("area of the right angle traingle is",area)

#GRADE LAB TASKS AT THE END OF DOCUMENT
#LAB TASK 1
number=int(input("enter the number"))
if number>0:
    print("the number is positive")
elif number<0:
    print("th number is negative")
elif number==0:
    print("the number is 0")

#LAB TASK 2
physics,chemistry,biology,mathematics,computer=eval(input("enter your marks in physics,chemistry,biology,mathematics and computer seperated by comma "))
if physics>100 or chemistry>100 or biology>100 or mathematics>100 or computer>100:
    print("you have entered incorrect marks.")
elif physics<=100 and chemistry<=100 and biology<=100 and mathematics<=100 and computer<=100:
    percentage=((physics+chemistry+biology+mathematics+computer)/500)*100
    if percentage>=90:
        print("GRADE A")
    elif percentage>=80:
        print("GRADE B")
    elif percentage>=70:
        print("GRADE C")
    elif percentage>=60:
        print("GRADE D")
    elif percentage>=40:
        print("GRADE E")
    elif percentage<40:
        print("GRADE F")

#LAB TASK 3
side1,side2,side3=eval(input("Enter the lenght of the three side os traingle seperated by comma"))
if side1==side2 and side2==side3 and side1==side3:
    print("triangle is equilateral")
elif side1!=side2 and side2!=side3 and side1!=side3:
    print("triangle is scalar")
else:
    print("triangle is isosceles")

#LAB TASK 4
correct_email="abc@gmail.com"
correct_password="abc"
email=input("enter your email")
password=input("enter the password")
if email!=correct_email and password!=correct_password:
    print("the email and password entered both are incorrect")
elif email==correct_email and password!=correct_password:
    print("password is incorrect")
elif email!=correct_email and password==correct_password:
    print("email entered is incorrect")
elif email==correct_email and password==correct_password:
    print("User is logged in")

#GRADED LAB TASK 5
year=int(input("enter the year you want to check for leap year"))
if year%4==0:
    print("the year is a leap year")
else:
    print("it is not a leap year")







