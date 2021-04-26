#connect to mysql database using python

#import the needed packages

import mysql.connector
from mysql.connector import Error

#define the connector functions
def connect_fetch():
    ''' function to connect and fetch rows in a database'''


    # create a variable for the connector object
    conn=None


    try:
        conn = mysql.connector.connect(host = 'localhost', database= 'cape_codd',
        user= 'Blackie2.0', password= 'mynameisblackie147')
        print('connecting to database server')
        if conn.is_connected:
            print('connected to database server')

            #select Query
            sql_select_query ="select * from buyer"
            cursor = conn.cursor(dictionary = True)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print('Total number of rows in buyer is: ', cursor.rowcount)

            #Display the output data
            print("\nPrinting each buyer record")
            for row in records:
                for i in row:
                    print (i, '-', row[i])
                print()    

    except Error as e:
        print('not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown')
connect_fetch()