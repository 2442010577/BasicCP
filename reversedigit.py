i=int(input("Enter a number: "))
reverse = 0
while i > 0:
    reverse = reverse * 10 + i % 10
    i //= 10

print("Reversed number:", reverse)
