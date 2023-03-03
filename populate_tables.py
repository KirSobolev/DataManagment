import mysql.connector as mysql

mydb = mysql.connect(host="localhost",
                     port="3306",
                     user="root",
                     password="ujveujveyj")
cursor = mydb.cursor()

cursor.execute("USE cd_shop;")
cursor.execute("INSERT INTO artist VALUES"
               "(1, 'lorem50'),"
               "(2, 'lorem10'),"
               "(3, 'lorem20');")

cursor.execute("INSERT INTO cd VALUES "
               "(1,'qweqwe', '5.2', 'eqdas', 1),"
               "(2,'qewads', '3.2', 'dasasd', 2), "
               "(3,'qdasweqwe', '52.2', 'edaszxqdas', 3);")

cursor.execute("INSERT INTO track VALUES"
               "(1, 'EQWEQW', 20, 1),"
               "(2, 'EQWEadQW', 25, 2),"
               "(3, 'EQWEadsQW', 490, 3);")
mydb.commit()
