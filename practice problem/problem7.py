#7.	Use a while loop to find the largest integer n such that n3 is less than 12,000.
n=1
cube=n*n*n
while cube<12000:
    n=n+1
    cube=n*n*n
print("the largest integer n such that n3 is less than 12,000 is",n-1)