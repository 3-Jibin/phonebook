import sqlite3    

connection = sqlite3.connect('phbook.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE phonebooks
              (slno INT,
                fname TEXT,
               lname TEXT,
                pno INT)''')

connection.commit()
connection.close()






