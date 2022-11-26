

# mark1 = float(input("Enter Mark 1"))
# mark2 = float(input("Enter Mark 2"))
# mark3 = float(input("Enter Mark 3"))
# mark4 = float(input("Enter Mark 4"))
# mark5 = float(input("Enter Mark 5"))
#
# total = mark1+mark2+mark3+mark4+mark5
# average = total / 5
# print(average)


marks_count = int(input("Enter Marks Count which you want to calculate"))
total = 0
for i in range(1,marks_count+1):
    while True:
        mark = float(input("Enter Mark "+str(i)))
        if 0 <= mark <= 100 :
            break
        else:
            print("Please Enter Mark Between 100 - 0")
    total += mark

average = total / marks_count
print(average)
if average >= 90:
    print("Your average = ",average,"  >> Excellent")
elif average >= 80:
    print("Your average = ", average, "  >> Very Good")
elif average >= 70:
    print("Your average = ", average, "  >> Good")
elif average >= 60:
    print("Your average = ", average, "  >> Mid")
elif average >= 50:
    print("Your average = ", average, "  >> Acceptance")
else:
    print("Your average = ", average, "  >> Failed")

