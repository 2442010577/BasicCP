angles = [int(input(f"Enter angle {i+1}: ")) for i in range(3)]
if sum(angles) == 180:
    if 90 in angles:
        print("Right triangle")
    elif all(a < 90 for a in angles):
        print("Acute triangle")
    else:
        print("Obtuse triangle")
else:
    print("Not a valid triangle")