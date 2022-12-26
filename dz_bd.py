#1 сформулируйте запрос для создания таблицы movies
#поля: movie_id, name TEXT, release_year INTEGER, genre TEXT
#2 создать функции:
# 1 добавить фильм(заполнение делать с клавиатуры)
# 2 получение данных обо всех фильмах
# 3 получения данных об одном фильме по id
#0 выход
#3 функции вызывать в цикле, чтоб у пользователя был выбор

import sqlite3

#
conn.sqlite3.connect('movies.db')

#курсор для взаимодействия с БД
cursor = conn.cursor()

movies.excute('''movie_id, name TEXT, release_year INTEGER, genre TEXT