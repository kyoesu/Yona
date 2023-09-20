import sqlite3





def sql_k(name):
    # Создаем подключение к базе данных (файл my_database.db будет создан)
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    # Создаем таблицу Users
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')



    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


sql_k("tg/Domino.db")