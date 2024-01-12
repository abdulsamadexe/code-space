# def format_name(firstname,lastname):
#     firstname=firstname.title()
#     lastname=lastname.title()
#     fullname=firstname +" "+ lastname
    
#     print(fullname)
#     return fullname

# format_name("abdul","samad")

#ADD
def add(n1,n2):
    return n1+n2
#subtract
def subtract(n1,n2):
    return n1-n2
#multiply
def multiply(n1,n2):
    return n1*n2
#division
def division(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division,
}
num1=int(input("enter the first number?"))
for i in operations:
    print(i)
operation_symbol=input("pick an operation from line above ")
num2=int(input("enter the second number?"))
for i in operations:
    if operation_symbol==i:
        result=operations[i](num1,num2)
print(f"{num1}{operation_symbol}{num2}={result}")
again=input("Do you want to continue? Press y for yes and n for no")
again=again.lower()
while again=="y":
    operation_symbol=input("pick an operation")
    num3=input("enter the second number")
    op=operations[operation_symbol]
    result2=op(result,num3)
    print(f"{result}{operation_symbol}{num3}={result2}")
    result=result2
    again=input("Do you want to continue? Press y for yes and n for no")
    again=again.lower()



