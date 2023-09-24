import sqlite3



'''def sql_begin():
    connection = sqlite3.connect("tg/Domino.db")# Создаем подключение к базе данных (файл my_database.db будет создан)
    cursor = connection.cursor()
    return cursor
def sql_end(connection):
    connection.commit()
    connection.close()'''

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

def sql_new_user(link,name):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM [Users] WHERE [link] = {link}")
    if not cursor.fetchall():
        cursor.execute(f"INSERT INTO [Users] ([name], [link]) VALUES ('{name}', '{link}')")

    connection.commit()
    connection.close()

def sql_new_age(link,age):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE [Users] SET [age] = {age} WHERE [link] = '{link}';")

    connection.commit()
    connection.close()

def sql_new_desk(link, desk):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE [Users] SET [else] = {desk} WHERE [link] = '{link}';")

    connection.commit()
    connection.close()


#при получении сообщения
def sql_get_mess(link,tex,name):
    import datetime
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT [id] FROM [Users] WHERE [link] = {link}")
    #print(cursor.fetchall())
    
    if cursor.fetchall():
        cursor.execute(f"INSERT INTO [mess] ([id-user],[text],[time]) VALUES ('{link}', '{tex}','{datetime.datetime.now()}')")
    else:
        sql_new_user(link,name)
        sql_get_mess(link,tex,name)

    connection.commit()
    connection.close()

def sql_show_his(link):
    connection = sqlite3.connect("tg/Domino.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT [text] FROM [mess] WHERE [link] = {link}")
    res=cursor.fetchall()
    connection.commit()
    connection.close()
    return res

