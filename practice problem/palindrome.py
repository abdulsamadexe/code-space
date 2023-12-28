s=input("Enter a string")
s=s.strip()
low=0
high=len(s)-1
while low<high:
    if s[low]==s[high]:
        low+=1
        high-=1
    else:
        print("its not a palindrome")
        break
if low>=high:
    print("Its a plaindrome")