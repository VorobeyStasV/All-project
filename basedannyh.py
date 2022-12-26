import sqlite3

#cursor & conn два основных наших


#создаем базу данных
conn = sqlite3.connect("name.db)

#оздаем объект cursor, который нам позволяет взаимодействовать с БД и
cursor = conn.cursor()

#создаем таблицу с двумя текстовыми колонками
cursor.execute("""CREATE TABLE IF NOT EXISTS tab_1
    (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1, TEXT, col_2, TEXT)""")

#заполням таблицу данными
cursor.excute("""INSERT INTO tab_1(col_1, col_2)""")
    VALUES ("hello", "world")"")

#сохраняем изменения
conn.commit()

d="red"
f="black"

#мы создали еще одну таблицу(можно скопировать предыдущую)
#
cursor.excute("""CREATE TABLE IF NOT EXISTS
    tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1, TEXT, col_2, TEXT)""")

cursor.excute("""INSERT INTO tab_1()col_1, col_2)
    VALUES (?,?)""")

conn.commit()
