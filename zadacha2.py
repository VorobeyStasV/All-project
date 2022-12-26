text = input('Введите текст: ')
v = []
n = 0
k = 0

for i in text:
    if i in ('ауоыэяюёие'):
        n += 1
        v.append(i)
    elif i in ('бвгджзйклмнпрстфхцчшщ'):
        k += 1

print('Гласные:', n, 'Согласные:', k)

if n == k:
    print('Все гласные буквы:', v)