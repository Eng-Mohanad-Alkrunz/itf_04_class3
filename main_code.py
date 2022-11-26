from utils import add_numbers,mul_numbers
import utils
from utils import *
import math
import random
from bank import Account

# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))
# print(x)
# print(add_numbers(num1,num2))
# print(mul_numbers(num1,num2))

x = 50
y = 20
z = 30
# min_num = x
# if x < y and x < z:
#     min_num = x
# elif y < z and y < x:
#     min_num = y
# else:
#     min_num = z
print(x,y,z)
print(min(x,y,z))
print(max(x,y,z))
print(abs(-5))
print( 5 ** 2)
print(pow(5,2))
print(math.pi)
print(math.ceil(10.3))
print(math.floor(10.3))
print(math.sqrt(25))
# print("Min Num. is ",min_num)

# m_random = random.Random()
# while True:
#     temp = int(m_random.random()*1000)
#     if temp >= 100 :
#         print(temp)
#         break


print(random.randint(1000,9999))