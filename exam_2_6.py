# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.

#first example

#print(len(set(int, input().split()) & (input().split())))

#two example
s = set(map(int, input().split()))
t = set(map(int, input().split()))
a = s & t
print(len(a))