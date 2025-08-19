perc = float(input("Enter percentage: "))
if perc >= 90:
    grade = "A"
elif perc >= 80:
    grade = "B"
elif perc >= 70:
    grade = "C"
elif perc >= 60:
    grade = "D"
elif perc >= 40:
    grade = "E"
else:
    grade = "F"
print("Grade:", grade)