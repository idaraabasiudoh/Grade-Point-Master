import string
# Grading system
grade_point = {'A+': 12.0, 'A': 11.0, 'A-': 10.0,
               'B+': 9.0, 'B': 8.0, 'B-': 7.0, 'C+': 6.0, 'C': 5.0, 'C-': 4.0, 'D+': 3.0, 'D': 2.0, 'D-': 1.0, 'F': 0.0}

allowed_grades = list(grade_point.keys())
allowed_credits = [0.25, 0.50, 0.75, 1.00]
cont = 'Y'
grades = []
credits = []


infile = open('My Grades.csv', 'r')
for line in infile:
    if line.strip('\n').split(",")[1] in grade_point:
        new_grade = line.strip('\n').split(",")[1]
        grades.append(new_grade)

        new_credit = float(line.strip('\n').split(",")[2])
        credits.append(new_credit)

GPA_point_sum = 0
credit_sum = 0
for i in range(len(grades)):
    GPA_point = grade_point[grades[i]] * credits[i]
    GPA_point_sum = GPA_point_sum + GPA_point
    credit_sum = credit_sum + credits[i]


CGPA = GPA_point_sum / credit_sum


print("Your current grades are ", grades)
print("Your total credit is ", credit_sum)
print("Your total GPA point ", GPA_point_sum)
print("\nYour current CGPA is ", CGPA)

