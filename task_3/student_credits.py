def students_credits(*args):
    result = ''
    courses = {}
    diploma_credits = 240
    student_all_credits = 0

    for i in args:
        data = i.split('-')
        current_course = data[0]
        total_credits = int(data[1])
        max_test_points = int(data[2])
        student_points = int(data[3])

        exam_credits = student_points / max_test_points * total_credits
        student_all_credits += exam_credits
        courses[current_course] = exam_credits

    credit_difference = abs(diploma_credits - student_all_credits)
    if student_all_credits >= diploma_credits:
        result += f"Diyan gets a diploma with {student_all_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {credit_difference:.1f} credits more for a diploma.\n"

    for k, v in sorted(courses.items(), key=lambda x: -x[1]):
        result += f"{k} - {v:.1f}\n"

    return result
