#connect to database and insert data
import mysql.connector
from mysql.connector import Error

def connect_insert():
    conn = None


    try:
        conn = mysql.connector.connect(host ='localhost', database = 'demolee2',
        user = 'Blackie2.0', password = 'mynameisblackie147')
        print('connecting to database server')
        if conn.is_connected:
            print('connected to the database')
            db_cursor = conn.cursor()
            sql = "insert into human(humanId, name, color, sex, bloodgroup) values (%s, %s, %s, %s, %s)"

            

            #create a list variable to contain all values we want to insert into human table

            val= []
            row_num = int (input('Enter amount of rows needed: '))
            for i in range(row_num):
                
                humanId = input('Enter humanID: ')
                name = input('Enter Name: ')
                color = input('Enter color: ')
                sex = input('Enter sex: ')
                bloodgroup = input('Enter bloodgroup: ')
                val.append((humanId, name, color, sex, bloodgroup))

            # val =[
            #     ('1013', 'Hannah', 'White', 'Female', 'B-'),
            #     ('1016',  'Micheal', 'Brown', 'Male', '0-'),
            #     ('1015', 'Sandy', 'Black', 'Female', 'B+')
            # ]

            #execute the query using the executemany function
            db_cursor.executemany(sql, val)

            #commit to database
            conn.commit()

            #print a success message
            print(db_cursor.rowcount, "row was inserted")

            #close the cursor
            db_cursor.close


    except Error as e:
        print('connection failed due to the following', e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
        print('Database shutdown')
connect_insert()