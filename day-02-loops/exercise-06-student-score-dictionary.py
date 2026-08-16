"""
Exercise: Student score dictionary
Student: Sabita Rajbanshi 
Day: 2

"""
# dictionary of five students and their scores
student_scores = {"Anisha": 78, "Ravi": 55, "Maya": 92, "Sagar": 61, "Nima": 48}

print("Students and Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

# creating a dictionary of students who scored at least 60 using dictionary comprehension
students_scoring_atleast_60 = {student: score for student, score in student_scores.items() if score >= 60}

# student with highest score using max() function
top_student = max(student_scores, key=student_scores.get)

# average score of all students
average_score = sum(student_scores.values()) / len(student_scores)

# outputs
print(f"\nStudents scoring at least 60: {students_scoring_atleast_60}\n")
print(f"Top student: {top_student}\n")
print(f"Average score: {average_score}\n")