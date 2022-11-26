# Enter Number of Students
# For Each of students >> Ask For Number Of Marks


students_count = int(input("Enter Number Of Students: "))
students_list = []
for i in range(1, students_count + 1):
    student = {}
    student_name = input("Enter Student Name")
    student['student_name'] = student_name
    marks_count = int(input("Enter Marks Number for student " + str(i) + " : "))
    student_marks_list = []
    total = 0
    for j in range(1, marks_count + 1):
        mark = float(input("Enter Mark " + str(j) + " : "))
        mark_name = input("Enter Mark Name")
        total += mark
        mark_dict = {
            "name" : mark_name,
            "mark" : mark
        }
        student_marks_list.append(mark_dict)
    student['marks'] = student_marks_list
    student['average'] = str(total / marks_count) + " %"
    students_list.append(student)
#
# print(students_list)
# for student in students_list:
#     print(student['marks'])
#
# student_dict = {
#     "student_name": "Mohanad",
#     "age": 27,
#     "nationality": "Palestinian",
#     "address": {
#         "city": "Gaza",
#         "street": "Al Quds",
#         "street_number": "52/8"
#     },
# }
#
#
# def get(test_dic,key):
#     if key in test_dic:
#         return test_dic[key]
#     else:
#         return None
#
#
# print("From Get Method ",get(student_dict,'age_1'))
#
# print(student_dict.get('age_1'))



# print(student_dict)
# for key,value in student_dict.items():
#     print(key,value)
# #
#
# print(student_dict['address']['city'], " -- ", student_dict['address']['street'])
# print(student_dict['age'])
# student_dict['age'] = 30
# student_dict['type'] = "Male"
# print(student_dict)
# print(student_dict["student_name"])
# print(student_dict["age"])
# print(student_dict.get('city'))
# print(student_dict.get('student_name'))


my_list = [10,20,30,40,50]
my_tuple = (10,20,30,40,50)
print(type(my_list))
print(type(my_tuple))
print(my_list[0])
print(my_tuple[0])
my_list[0] = 100
print(my_list)

print(my_tuple)