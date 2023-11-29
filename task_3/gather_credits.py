def gather_credits(needed_credits, *courses_data):

    courses = []
    current_credits = 0

    for course_name, points in courses_data:
        if current_credits >= needed_credits:
            break
        if course_name in courses:
            continue

        courses.append(course_name)
        current_credits += points

    if current_credits >= needed_credits:
        return f"""Enrollment finished! Maximum credits: {current_credits}.
Courses: {', '.join(sorted(courses))}"""
    return f"You need to enroll in more courses! You have to gather {needed_credits - current_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))



