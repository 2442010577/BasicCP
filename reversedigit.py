i=int(input("Enter a number: "))
reverse_i = 0
while i > 0:
    reverse_i = reverse_i * 10 + i % 10
    i //= 10
print("Reversed number:", reverse_i)