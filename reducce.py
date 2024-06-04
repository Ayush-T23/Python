from functools import reduce
number=[float(input(f"Enter numbers {i+1} :"))for i in range(10)]
sum=reduce(lambda x,y:x+y,number)
print(f"The sum of numbers is : {sum}")