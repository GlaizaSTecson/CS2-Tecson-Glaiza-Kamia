students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

totalclass_average = 0 

for i in range(1, students + 1):
    print(f"\nStudent {i}")
    total_score = 0

    for j in range(1, subjects + 1):
        score = float(input(f"Enter score {j}: "))
        total_score += score

    average = total_score / subjects
    print(f"Average for Student {i} = {average:.1f}")

    totalclass_average += average

class_average = totalclass_average / students
print("Class Average = “, class_average)
