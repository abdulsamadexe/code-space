import random
c="listen"
i=1
num=int(input('enter number'))
while i<=num:
    print(i*"*")
    i=i+1
while i!=1:
    i=i-1
    print("*"*i)
    

# def sad(x):
#     for a in range(x):
#         for b in range(x):
#             number=random.randint(0,1)
#             print(number,end=' ')
#         print()
# import random
# a=int(input('number'))
# def sad(x):
#     sum=0
#     for a in range(1,x):
#         if x%a==0:
#             sum=sum+a
#     if sum==x:
#         print(x,'is a sad number')
#     else:
#         print(x,'is not a sad number')
# sad(a)
# def anagram(s1,s2):
#     a=False
#     for sad in s1:
#             if sad not in s2:
#                 print(s1,'and',s2,'are not anagrams')
#                 a=False
#                 break
#             else:
#                 a=True
#     for i in s2:
#         if i not in s1:
#                     print(s1,'and',s2,'are not anagrams')
#                     a=False
#                     break
#         else:
#                 a=True
            
#     if a==True:
#         print(s1,'and',s2,'are anagrams')
# s1='silent'
# s2='silentlisten'                

# print(s2)
# anagram(s1,s2)
# n=eval(input('number'))
# number=9
# sum=0
# for i in range(n):
#     sum=sum+number
#     number=number*11
# print(sum)


    