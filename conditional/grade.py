marks = int(input("Enter your marks to get your grade: "))

if marks >= 90:
    grade = "A"
elif marks >= 89:
    grade = "B"
elif marks >= 79:
    grade = "C"
elif marks >= 69:
    grade = "D"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Your grade is: ", grade)
