n=5
for i in range (n+1):
    for j in range(1,7, n+1):
        if j==1 or j==7-n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()