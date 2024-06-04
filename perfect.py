n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
    
print(" program created by : Ayush Tiwari . \n Course=Bca. \n section=F1. \n semester = 4. \n Rollno = 25.")