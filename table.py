class PhoneBooks:

    def main():
     
        a = input("""      1.  ADD
        2.  LIST
        3.  UPDATE
        4.  DELETE  """)


    
  
    def add():    
        
        import sqlite3
        connection = sqlite3.connect('phbook.db')
        cursor = connection.cursor()

        sl_no = input('Enter sl. no.')

        f_name = input('First name:')

        l_name = input('Last Name:')

        p_no = input('Phone number')

        cursor.execute("""
        INSERT INTO phonebooks(slno, fname, lname, pno)
        VALUES (?,?,?,?)
        """, (sl_no, f_name, l_name, p_no))

        connection.commit()

        connection.close()
    
     

    def lists():  
        
        import sqlite3
        connection = sqlite3.connect('phbook.db')
        cursor = connection.cursor()
    
        cursor.execute("SELECT * FROM phonebooks")
        print(cursor.fetchall())


        connection.commit()

        connection.close()

    def delete():

        import sqlite3
        connection = sqlite3.connect('phbook.db')

        cursor = connection.cursor()

        slno = input("Enter the correct sl no. to need delete")

        cursor.execute("DELETE FROM phonebooks WHERE slno =  slno")

        print("The ROW",slno,"deleted succecfully")

        cursor.execute("SELECT * FROM phonebooks WHERE slno = slno")

        print(cursor.fetchall())

        connection.commit()

        connection.close()

p = PhoneBooks

p.main()
a = 5
if a == 1: 
    p.add()

    
git remote add origin https://github.com/3-Jibin/requirements.txt.git
git branch -M main
git push -u origin main





    
    


     

        