class Car:
    def __init__(self, color, type, year):
        self.year = year
        self.type = type_car
        self.color = color

    def func_a(self):
        print("car work")

    def func_b(self):
        print("car off")

    def func_c(self):
        print("year car", year)

    def func_d(self):
        print("year car", type_car)


    def func_color(self):
        print(self.color)

year = input("введите год")
typec_car = input("Введите тип")
color = input("Введите цвет")
car = Car(year, type, color)
car.func_year