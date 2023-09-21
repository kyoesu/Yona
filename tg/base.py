import sqlite3



def sql_begin():
    connection = sqlite3.connect("tg/Domino.db")# Создаем подключение к базе данных (файл my_database.db будет создан)
    cursor = connection.cursor()
    return cursor
def sql_end(connection):
    connection.commit()
    connection.close()

def sql_adm():
    
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    
    cursor.execute('''
SELECT *
FROM [Users]
ORDER BY [id] DESC LIMIT 500
''')


    res=cursor.fetchall()
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()
    return res

def sql_new_user(id,name):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (name, link) VALUES ('{name}', '{id}')")

    connection.commit()
    connection.close()

def sql_new_age(id,age):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE users SET age = {age} WHERE link = '{id}';")

    connection.commit()
    connection.close()

def sql_new_desk(id, desk):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE users SET else = {desk} WHERE link = '{id}';")

    connection.commit()
    connection.close()
#print(sql_k())