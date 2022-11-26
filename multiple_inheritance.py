class ParentClass:

    def __init__(self):
        self.a_var = "a from parent"

    def feature_1(self):
        print("Feature 1 from parent")


class ParentClass2 :
    def __init__(self):
        self.c_var = "c from parent2"

    def feature_3(self):
        print("Feature 3 from parent2")


class ChildClass(ParentClass,ParentClass2):

    def __init__(self):
        super().__init__()
        self.b_var = "b var from Child"


    def feature_2(self):
        print("Feature 2 from child Class")