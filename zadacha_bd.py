# создайе новую БД
# в ней создайте таблицу с тремя полями, два текстовых, одно - целое число
# число запрашивается с клавиатуры, а слова задаются статтически.
# * введите каждую запись в отдельную строку

import sqlite3

a = input()

conn = sqlite3.connect("task_1.db)

#создаем объект cursor, который нам позволяет взаимодействовать с БД и
cursor = conn.cursor()

#создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS task_1
    (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INT)''')

cursor.execute('''INSERT INTO tab_1(col_1, col_2, col_3)
    VALUES ("HELLO", "WORLD", ?)''', (a,))
conn.commit()

cursor.execute('''SELECT*FROM task_1''')
k = cursor.fetchall()
print(k)
for i in k:
    c = ','.join([str(x) for x in i])
    print(c)