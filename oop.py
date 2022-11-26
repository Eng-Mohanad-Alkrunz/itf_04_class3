
name = "Ali"

x = 10


class Car:
    x = 0

    def __init__(self,car_number,car_color="White"):
        self.car_color = car_color
        self.car_number = car_number
        self.speed = 0




    def speed_up(self,speed):
        self.speed += speed

    def speed_down(self):
        self.speed -= 10

car1_object = Car(car_color="Yellow",car_number="2020")
car2_object = Car(car_color="Black",car_number="2040")

print(car1_object.car_color)
print(car1_object.car_number)

print(car2_object.car_color)
print(car2_object.car_number)
car1_object.speed_up(40)
print(car1_object.speed)
print(car2_object.speed)
car1_object.speed_up(20)
print(car1_object.speed)
car1_object.speed_down()
car2_object.speed_up(30)
car2_object.speed_down()
print(car1_object.speed , " Car 1 Speed")
print(car2_object.speed, " Car 2 Speed")
