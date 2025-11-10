import sys

# If user gives 5 marks as arguments, use them
if len(sys.argv) == 6:
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    m3 = float(sys.argv[3])
    m4 = float(sys.argv[4])
    m5 = float(sys.argv[5])
else:
    # Default marks (if no input given)
    print("No input provided. Using default marks: 80, 75, 90, 85, 70")
    m1, m2, m3, m4, m5 = 80, 75, 90, 85, 70

# Calculate average
avg = (m1 + m2 + m3 + m4 + m5) / 5

# Determine grade
if avg >= 90:
    grade = 'A'
elif avg >= 75:
    grade = 'B'
elif avg >= 60:
    grade = 'C'
elif avg >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Display output
print("Average Marks:", avg)
print("Grade:", grade)
