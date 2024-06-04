si=lambda p,r,t:(p*r*t)/100
r=6.58
principal=float(input("Enter the principal"))
time=float(input("Enter the time"))
interest=si(principal,r,time)
print("The Interest is: ",interest)