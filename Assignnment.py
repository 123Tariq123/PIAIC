def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


student_score = 95  # Replace with the student's actual score
grade = calculate_grade(student_score)
print(f"The student's grade is: {grade}")


# Abdussamad_score=input(50)
# Abdulahad_score=input(65)
# Waniyatariq_score=input(70)
# Aliyatariq_score=input(95)
# Bushrafaruqui_score=input(10)
# Anashassan_score=input(54)
# Laibahassan_score=input(85)
# Tehreemhassan_score=input(88)
# Tariq_score=input(5)

# def calculate_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"

# student_score = 18  # Replace with the student's actual score
# grade = calculate_grade(student_score)
# print(f"The student's grade is: {grade}")