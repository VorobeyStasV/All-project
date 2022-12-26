#Напишите программу, демонстрирующую работу try\except\finally

s = open("stas.txt")
ints = []
try:
    for line in s:
        ints.append(int(line))
except ValueError:
    print("не число, выход")
except Exception:
    print("Это не то")
else:
    print("хорошо")
finally:
    f.close()
    print("Я закрыл файл")