class example: #создаем класс
    a = 2 #создание статические атрибута
    b = 3
    def __init__(self, t, r): #инициализация объектов
        self.t = t #
        self.r = r
    def func(self):   #создание функции (в которой делаем сумму статических атрибутов)
        self.c = 5
        print(self.c)
    def func_1(self): #создание функции (в которой делаем сумму статических атрибутов)
        self.t + self.r

    def func_2(self): #создание произведения динамических атрибутов
        return self.t ** self.r

example1 = example(4, 2) #динамический атрибут объектов (возводим 4 вот 2 степень, для умножения)
print(example1.a)
print(example1.func_1())
print(example1.func_2())
example1.func() #закрываем функции