#!/usr/bin/python
# -*- coding: utf-8
import MySQLdb
import string

# соединяемся с базой данных
db = MySQLdb.connect(host="localhost", user="root", passwd="toor", db="yii2basic", charset='utf8')
# формируем курсор
cursor = db.cursor()

# запрос к БД
sql = """SELECT * FROM taxes"""
# выполняем запрос
cursor.execute(sql)

# получаем результат выполнения запроса
data =  cursor.fetchall()
# перебираем записи
for rec in data:
    # извлекаем данные из записей - в том же порядке, как и в SQL-запросе
    #name, surname, balance = rec
    # выводим информацию
    print rec[2]

# закрываем соединение с БД
db.close()