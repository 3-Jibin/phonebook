import sqlite3


class PhoneBooks:

    def con(self):
        self.connection = sqlite3.connect('phone.db')
        self.cursor = self.connection.cursor()
        

    def main(self):
     
        a = int(input("""        1.  ADD
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


    
  
    def add(self):    
        
        

        f_name = input('First name:')

        l_name = input('Last Name:')

        p_no = input('Phone number')

        self.cursor.execute("""
        INSERT INTO phonebooks(fname, lname, pno)
        VALUES (?,?,?)
        """, (f_name, l_name, p_no))

        
    
    

    def lists(self):  
        
           
        self.cursor.execute("SELECT * FROM phonebooks")


        books = self.cursor.fetchall()

        print("ROW" + "\tNAME" + "\t\t\tPHONE NUMBER")
        print("----"+"\t-----"+"\t\t\t-------------")

        for book in books:
            print(str(book[0])+"\t"+book[1]+" "+book[2]+" \t \t"+str(book[3]))


        

    def delete(self):

        r_no = input("Enter the Row number to Delete:")

        self.cursor.execute("DELETE FROM phonebooks WHERE slno = {}".format(r_no))

        self.print("The Row"+ r_no +" deleted succecfully")

        self.cursor.execute("SELECT * FROM phonebooks")

        print(self.cursor.fetchall())

            

    def update(self):
        

        rno = input("Enter the Row number  :")
        print(type (rno))
        self.cursor.execute("""UPDATE phonebooks SET pno = 90909091111 
                
                        WHERE slno = {}""".format(rno))

        self.cursor.execute("SELECT * FROM phonebooks ")

        books = self.cursor.fetchall()

        print("ROW" + "\tNAME" + "\t\t\tPHONE NUMBER")
        print("----"+"\t-----"+"\t\t\t-------------")

        for book in books:
            print(str(book[0])+"\t"+book[1]+" "+book[2]+" \t \t"+str(book[3]))


    def close(self):
        self.connection.commit()
        self.cursor.close()

        self.connection.close()
      

p = PhoneBooks()
p.con()
p.main()
p.close()





    
    


     

        