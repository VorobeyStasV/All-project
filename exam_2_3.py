#Даны два кортежа:
#C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
#C_2 = (45, 21,124,76,5,23,91,234)
#Необходимо определить:
#1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже -)
#2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей

c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)

s1 = sum(c_1)
s2 = sum(c_2)

if s1 > s2:
    print("Сумма  больше в картеже c_1")
else:
    print("сумма больше в кортеже c_2")
print("min c_1", min(c_1), "Номер - ", c_1.index(min(c_1)) + 1)
print("max c_1", max(c_1), "Номер - ", c_1.index(max(c_1)) + 1)
print("min c_2", min(c_2), "Номер - ", c_2.index(min(c_2)) + 1)
print("max c_2", max(c_2), "Номер - ", c_2.index(max(c_2)) + 1)