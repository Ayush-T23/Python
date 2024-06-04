count = 0
for num in range(2, 101):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num)
        count += 1
print("Total Prime numbers between 1 to 100:", count)
