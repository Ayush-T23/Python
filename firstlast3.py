l1=[]
for i in range (0,7):
    v1=int(input("Enter the list element"))
    l1.append(v1)
print("The list elements are: ",l1)
l3=l1[-3:]
print("The last 3 elements are: ",l3)
f3=l1[:3]
print("The first 3 elements are: ",f3)
fl=l1[1:-1]
print("The list without first and last element is: ",fl)
