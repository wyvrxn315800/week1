survey_results = [
    ["Python","Javascrip","c++"],
    ["Python","Javascrip","c#"],
    ["python","java"],
    ["Python","Javascrip","c++"],
    ["Python","Javascrip","c++","Java"]
]
attendance_sets = [set(day) for day in survey_results]
print(attendance_sets)
present_evert_day = set.intersection(*attendance_sets)
print("Present every day:",present_evert_day)
all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students-present_evert_day
print("Absent at least one day:",absent_at_least_one_day)
first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:",first_day_but_not_last)
unique_students_count = len(all_students)
print("particippants with the same set of language:",unique_students_count)