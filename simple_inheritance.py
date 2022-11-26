class ParentClass:

    def __init__(self):
        self.a_var = "a from parent"

    def feature_1(self):
        print("Feature 1 from parent")


class ChildClass(ParentClass):

    def __init__(self):
        super().__init__()
        self.b_var = "b var from Child"

    def feature_2(self):
        print("Feature 2 from child Class")
