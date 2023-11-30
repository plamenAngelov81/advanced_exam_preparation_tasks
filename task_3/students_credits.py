def students_credits(*args):
    course_data = {}

    current_credits = 0

    for i in args:
        students_data = i.split('-')
        course = students_data[0]
        max_credits_per_course = int(students_data[1])
        max_points = int(students_data[2])
        exam_points = int(students_data[3])
        exam_credits = exam_points / max_points * max_credits_per_course
        current_credits += exam_credits
        if course not in course_data:
            course_data[course] = exam_credits
    result = ''
    if current_credits >= 240:
        result += f"Diyan gets a diploma with {current_credits:.1f} credits.\n"
    else:
        need_credits = 240 - current_credits
        result += f"Diyan needs {need_credits:.1f} credits more for a diploma.\n"

    for k, v in sorted(course_data.items(), key=lambda x: -x[1]):
        result += f"{k} - {v:.1f}\n"

    return result

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)