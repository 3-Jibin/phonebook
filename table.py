import sqlite3

connection = sqlite3.connect('phone.db')
cursor = connection.cursor()
class PhoneBooks:

    def main():
     
        a = int(input("""      1.  ADD
        2.  LIST
        3.  DELETE
        4.  UPDATE  """))

        if a == 1: 
            p.add()

        elif a == 2:
            p.lists()

        elif a == 3:
            p.delete()

        elif a == 4:
            p.update()


    
  
    def add():    
        
        

        f_name = input('First name:')

        l_name = input('Last Name:')

        p_no = input('Phone number')

        cursor.execute("""
        INSERT INTO phonebooks(fname, lname, pno)
        VALUES (?,?,?)
        """, (f_name, l_name, p_no))

           
    

    def lists():  
        
           
        cursor.execute("SELECT * FROM phonebooks")


        books = cursor.fetchall()

        print("ROW" + "   NAME " + "\t\t PHONE NUMBER")
        print("----------"+"\t\t-------------")

        for book in books:
            print(book)

             

    def delete():

        r_no = input("Enter the Row number to Delete you want:")

        cursor.execute("DELETE FROM phonebooks WHERE slno = {}".format(r_no))

        print("The Row"+ r_no +" deleted succecfully")

        cursor.execute("SELECT * FROM phonebooks")

        print(cursor.fetchall())

        

    def update():
        
        rno = input("Enter the Row number  :")
        print(type (rno))
        cursor.execute("""UPDATE phonebooks SET pno = 90909091111 
                
                        WHERE slno = {}""".format(rno))

        cursor.execute("SELECT * FROM phonebooks")

           
    
        print(cursor.fetchall())


        



p = PhoneBooks

p.main()
    
connection.commit()
cursor.close()


connection.close()






    
    


     

        