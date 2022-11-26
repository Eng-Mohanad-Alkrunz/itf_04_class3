import random

class ParentClass:

    def __init__(self):
        self.a_var = 10

    def  feature_1(self):
        print("Feature 1 from Parent class")


class ParentClass2:

    def __init__(self):
        self.b_var = 20

    def feature_3(self):
        print("Feature 3 from Parent 2")


class ChildClass(ParentClass2,ParentClass):

    def __init__(self):
        super().__init__()
        self.c_var = 40

    def feature_2(self):
        print("Feature 2 from Child Class")


parent_class = ParentClass()

child_class = ChildClass()
parent_class.feature_1()
child_class.feature_2()
child_class.feature_1()




class Person:
    def __init__(self,full_name,age,mobile_number):
        self.id = random.randint(1000,9000)
        self.full_name = full_name
        self.age = age
        self.mobile_number = mobile_number


class FullTimeEmployee(Person):


    def __init__(self, salary, full_name, age, mobile_number):
        super().__init__(full_name, age, mobile_number)
        self.salary = salary



class PartTimeEmployee():
    pass

# person = Person(age=10,full_name="Mohanad",mobile_number="45665")

# person.salary

# full_time_obj = FullTimeEmployee(age=10,full_name="Mohanad",mobile_number="45665")
# full_time_obj.salary

# print(full_time_obj.)
# part_time_obj = PartTimeEmployee()
