import mysql.connector
from mysql.connector import Error

def connect_fetch():
    conn = None


    try:
        conn = mysql.connector.connect(host ='localhost', database = 'demolee2',
        user = 'Blackie2.0', password = 'mynameisblackie147')
        print('connecting to database server')
        if conn.is_connected:
            print('connected to database server')

            sql_select_query ="select * from human"
            cursor = conn.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print('Total number of rows in human is: ', cursor.rowcount)

    except Error as e:
        print('not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown')
connect_fetch()        