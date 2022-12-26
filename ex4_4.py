# class Nikola(self, name, age)
#     __shots__= ["name", 'age']
#     def __init__(self, name, age):
#         if name  == "Николай"
#             self.name

# class Test:
#     __test = 0
#
# print(Test.__test)

#zadacha_test
class test:
    def print_text(self):
        print("то дочерний класс")
class Test1(Test):
    def print_text(self):
        print("это дочерний класс")
test2 = Test1()
test2.print_text()