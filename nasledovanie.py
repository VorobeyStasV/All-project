#
#
#

#

class foo:
    def foo_method(self):
        print("это родительский метод из класса Foo")

#создание класса foo 2, которое будет наследовать Foo

class Foo_2(Foo):
    def foo_2_method(self):
        print("Это метод из дочерного класса")

# создаем класс Foo_3(Foo_2)

class Foo_3(Foo_2):
    def foo_3Method(self):
        print("этодочерний метод из класса Foo_2")

