
def sum_num(list_num, total):
    for i in range(len(list_num)):
        for j in range(i+1, len(list_num)):
            sum_2 = list_num[i] + list_num[j]
            if sum_2 == total:
                return [i, j]


nums = []
list_length = int(input("Enter the list length"))

for i in range(list_length):
    num = int(input("Enter a number to the list"))
    nums.append(num)


target = int(input("Enter the target"))

print("the list of numbers", nums)
print("The indexes of the target numbers", sum_num(nums, target))