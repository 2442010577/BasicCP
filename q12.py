angles = [int(input(f"Enter angle {ch}: ")) for ch in ['A', 'B', 'C']]
if sum(angles) == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")