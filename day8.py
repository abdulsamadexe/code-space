import math
# def greet():
#     print("how")
#     print("are")
#     print("you?")

# greet()
# def name(name):
#     print(f"hi {name}")
#     print(f"how are you {name}")
# name("samad")

# def name_list(name,location):
#     print(f"hi {name}")
#     print(f"how is it in {location}")
# name_list(location="kamra",name="samad")

# given_height=int(input("Enter the height of the wall"))
# given_width=int(input("Enter the width of the wall"))
# coverage=5
# def no_of_cans(height,width,total_coverage):
#     no_of_cans=(height*width)/coverage
#     print(f"The no of cans required for the purpose are {no_of_cans}")
#     no_of_cans=math.ceil(no_of_cans)
# no_of_cans(height=given_height,width=given_width,total_coverage=coverage)
# loop=int(input("if you want to repeat the operation press 1"))
# while loop==1:
#     given_height=int(input("Enter the height of the wall"))
#     given_width=int(input("Enter the width of the wall"))
#     coverage=5
#     no_of_cans(height=given_height,width=given_width,total_coverage=coverage)
#     x=int(input("if you want to repeat the operation press 1"))
#     if x!=1:
#         loop=loop+1


# prime nmber checker

# n=int(input("check this number :"))
# def prime_number_checker(number):
#     x=n-1
#     is_prime=True
#     while x>1 and x!=n:
#         if n%x==0:
#             is_prime=False        
#         x=x-1
#     if is_prime==True:
#         print(f"{n} is prime")
#     else:
#         print(f"{n} is not a prime number")
# prime_number_checker(number=n)

# i=0
# display=[]
# ascending_order=[]
# while i<15:
#     a=int(input("enter a number :"))
#     display.append(a)
#     i=i+1
# print(display)
# for i in display:
#     while len(display)!=len(ascending_order):
#         for y in display:
#             if i<y:
#                 ascending_order.append(i)
#                 display.remove(i)
# print(ascending_order)
        
# Function to take 15 values as input
def take_input():
    values = []
    for i in range(15):
        value = int(input(f"Enter value {i + 1}: "))
        values.append(value)
    return values
def ascending(values):
    values=sorted(values)
    print("ascending values",values)
def descending(values):
    values=sorted(values,reverse=True)
    print("descending values",values)

input_values=take_input()
ascending(input_values)
descending(input_values)



        



