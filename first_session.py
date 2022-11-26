num_1 = int(input("Enter First Number"))
num_2 = int(input("Enter Second Number"))


if num_1 > 0 and  num_2 > 0 :
    if num_1 > 100:
        print("Number 1 is larger than 100")
    elif num_1 > 50 :
        print("Number 1 is larger than 50")
    else:
        print("Number 1 is smaller than 100")
    print("Numbers are Positive")
    print(num_1/num_2)
elif num_1 > 0:
    print("Number 1 is Positive",num_1)
    print("Number 2 is Negative",num_2)
elif num_2 > 0:
    print("Number 2 is Positive", num_2 , "Number 1 is Negative", num_1)
else:
    print("Numbers are negative")
    print(num_1 * num_2)

print("Done")


