for i in range (5):
    for j in range(7-i):
        if j==0 or j==7-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()