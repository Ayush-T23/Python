sum=0
n=(int(input("Enter a no")))
temp=n
while(n):
    x=1
    fact=1
    r=n%10
    for x in range(1,r+1):
        fact=fact*x
    sum=sum+fact
    n=n//10
if(sum==temp):
    print("strong")
else:
    print("not strong")