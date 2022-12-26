# # power = lambda x, y: x * y
# # print(power(2, 3))
#
# def foo(x):
#     def fool(y):
#         rerturn x + y
#     return fool(y)
#
# print(foo(3)(2))

# def first_test():
#     print("test function 1")
# def second_test():
#     print("test function 2")
#
# def simple_decore(fn)
#     #передаем аргумент
#     #исаользуем функцию в функцию
#     def wrapper():
#         print("start function")   #старт функции, тест, снова возвращается к функции, потом старт, проверяем вторую функцию
#         fn()
#         print("Stop function")
#         #передаем функцию старт
#         return wrapper
#         # first_test_wrapper = simple_decore(simple_decore())
#         # second_test = simple_decore(second_test())
#     #расширяем возможности
#     @simple_decore #декоратор, упрощает код
#     def first_test():
#         print("test function 1")
#
#     first_test()


# def param_transfer(fn):  #fn - аргумент
#     def wrapper(arg):
#         print("start function: ", str(fn.__name__) + "(), with param: " + str(arg))
#         fn(arg)
#
#     return
#
# @param_transfer()
# def print_sqrt(num):
#     print(num ** 0.5)
#
#     print_sqrt(4)


#написать функцию, которая определяет количество разрядов введенного целого числа
# def digits(n):
#     return len(str(n))
# num = int(input("введите число: "))
# print("количтво разрядов: ", digits(num))


#создайте функцию, которая принимает на вход неограниченное кол-во позиционных и именованных параметров
#в качестве результата функция должна возвращать только позицицонные параметры с нечетными индексами и ключевые,
#значения которых являются строками

a = []
b = []

def fun(*args, **kwargs):
    for i in args:
        if args.index(i) % 2 != 0:
            a.append(i)
    for value in kwargs.values():
        if type(value) is str:
            b.append(value)

    return a, b
print(fun(1, 2, 3, 4, 5, name = "Mike", job = "programmer", num = 123))