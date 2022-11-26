

# while True:
#     try:
#         num = int(input("Enter Integer Number"))
#         break
#     except:
#         print("Please Enter Valid Number")
#
# total = num * 2
# print(total)
# while True:
#     student_level = input("Select Student Level : [A-B-C] ")
#     if student_level in ("A","B","C"):
#         break
#     print("Invalid Selection")
# print("Student Level = ",student_level)


while True:
    try:
        x = int(input("1. Create Student\n2. Update Student\n3. Delete Student"))
        if x in (1,2,3):
            break
        else:
            print("Invalid Input")
    except:
        print("Invalid Input")

print("Bye Bye")