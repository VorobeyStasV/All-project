# def a_func():
#     print("hello")
# a_func()

# def a_func():#пустая функция
#     pass #закрыть функцию


#вывести функцию. посчитать список
# arr = [1, 2, 3, 4, 5]
# def foo():
#     c = 0
#     for i in arr:
#         c += i
#     print("sum", c)
# foo


# def foo(a, b):
#     return a + b
# print(foo(1, 2))

# def keyword_function(a, b=4, c=5):
#     return a + b + c
# print(keyword_function(b=4, c = 5))
# print(keyword_function(1, b = 4, c = 5))
# print(keyword_function(1))


# def many(*args, **kwargs):
#     print(args)#только на value
#     print(kwargs)#использует ключ значение(как словарь)
#
# many(1, 2, 3, name = "mike", job = "programmer")

#видимость!!!
#local
# def foo_a():
#     a =1
#     b=2
#     return a + b
# def foo_():
#     c = 5
#     rerturn a + c
# print(foo_a)
# print(foo_())

# def foo_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
# def foo_v():
#     c = 5
#     rerturn a + c
# print(foo_a)
# print(foo_v)


# def foo(a, b):
#     def foo_1(x):
#         return x * x * x
#     return foo_1(a) +foo_1(b)
# print(foo(4, 5))

#высокосный или нет
# def is_year_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year // 400 == 0
# print(is_year_leap(int(input("введите год"))))

#времена года.
# def season(num):
#     if num == 12 or 1 <= num <= 2:
#         print("winter")
#     elif 3 <= num <= 5:
#         print("bring")
#     elif 6 <= num <= 8:
#         print("summer")
#     elif 9 <= num <= 11:
#         print("otumn")
