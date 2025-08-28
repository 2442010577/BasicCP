n = int(input())
d = int(input())

count = 0
while n > 0:
    last = n % 10
    if last == d:
        count += 1
    n //= 10

print(count)

n=5
for i in range(1,n+1):
    print(" "*i end="")
    print("*"*)