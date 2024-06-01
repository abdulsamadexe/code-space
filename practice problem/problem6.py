# 6.	Write a program that displays, ten numbers per line, all the numbers from 100 to 200 that are divisible by 5 or 6, but not both. The numbers are separated by exactly one space
numbers=[]
for i in range(100,201):
    if (i%5!=0 or i%6!=0):
        if i%5==0 or i%6==0:
            numbers.append(i)
    numbers=sorted(numbers)
i=0
a=0
while a<=len(numbers):
    print(numbers[a],end=" ")
    if (a+1)%10==0 and a!=0:
        print("\n")
    a=a+1

x=int(input("Enter first number"))
y=int(input("Enter second number"))
if x>y:
    print(x,"is greater than",y)
else:
    print(y,"is greater than",x)



