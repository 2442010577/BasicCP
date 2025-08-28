rows=int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)
rows = 5
for i in range(1, rows + 1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)

