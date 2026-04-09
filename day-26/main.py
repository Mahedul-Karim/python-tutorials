import random

numbers = [4,8,2]

new_numbers = [num + 2 for num in numbers]

new_numbers_condition = [num + 2 for num in numbers if num > 2]
print(new_numbers_condition)

students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores={student:random.randint(1,100) for student in students}
print(students_scores)

passed_students={student:score for (student,score) in students_scores.items() if score >= 33}
print(passed_students)