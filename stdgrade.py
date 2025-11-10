import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    marks = [float(sys.argv[i]) for i in range(1, 6)]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    marks = [85, 78, 92, 88, 76]  # default marks
    print("No input given - using default values:")

# Calculate average
average = sum(marks) / 5

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

print("Script name:", script_name)
print("Marks:", marks)
print("Average Marks:", average)
print("Grade:", grade)
