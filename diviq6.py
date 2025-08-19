i=int(input("Enter a number: "))
sum=0
for i in range(1,i+1):
    if i % 2 == 0:
        sum += i
print("Sum:", sum)