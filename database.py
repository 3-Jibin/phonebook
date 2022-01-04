import sqlite3    

connection = sqlite3.connect('phone.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE phonebooks
              ( slno INTEGER PRIMARY KEY,
              
                fname TEXT,
               lname TEXT,
                pno INT)''')

connection.commit()
connection.close()






