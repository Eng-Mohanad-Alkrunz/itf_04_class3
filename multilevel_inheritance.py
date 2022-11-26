class ParentClass:

    def __init__(self):
        self.a_var = "a from parent"

    def feature_1(self):
        print("Feature 1 from parent")


class ChildClass1(ParentClass):

    def __init__(self):
        super().__init__()
        self.b_var = "b var from Child 1"


    def feature_2(self):
        print("Feature 2 from child Class 1")


class ChildClass2(ChildClass1):

    def __init__(self):
        super().__init__()
        self.c_var = "c var from Child 2"


    def feature_3(self):
        print("Feature 3 from child Class2")

parent_class = ParentClass()
child1_class = ChildClass1()
child2_class = ChildClass2()
print(child2_class.a_var)