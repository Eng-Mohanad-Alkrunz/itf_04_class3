from abc import abstractmethod


class Shape:
    pass
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def get_area(self):
        return 10

    def get_name(self):
        return "Rectangle"


