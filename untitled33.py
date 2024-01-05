print("There are 3 subjects rated this semester")

# List of subjects
subjects = ["biology", "Mathematics", "chemistry"]
length_subjects = len(subjects)
print(length_subjects)

# List of names of students
students = ["salim", "Ilhaam", "Nabeel", "Ilyaas", "Mohammed"]
length_students = len(students)
print("There are", length_students, "students")

# Sort students
students.sort(key=str.lower)

# Dictionary of students with grades
students_with_grades = {
    "salim":  (90, 80, 75), 
    "Ilhaam":  (60, 70, 80), 
    "Nabeel":  (90, 70, 75), 
    "Ilyaas":  (90, 70, 65), 
    "Mohammed":(78, 60, 50)
}

overall_average = 0

for name in students:
    if name in students_with_grades:
        score = students_with_grades[name]
        average = sum(score) / length_subjects
        print(average)
        print(score)
        #add overal average
        overall_average +=average
    else:
        print("None")

overall_average = average / length_students
print(f"Overall Average: {round(overall_average, 2)}")
    