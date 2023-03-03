import mysql.connector as mysql

mydb = mysql.connect(host="localhost",
                     port="3306",
                     user="root",
                     password="ujveujveyj")
cursor = mydb.cursor()


def create_db(*db_names):
    # For each argument given creates new database with given name if not exists
    for database in db_names:
        sql = F"CREATE DATABASE IF NOT EXISTS {database}"
        cursor.execute(sql)


bookshop_ddl = ["USE bookshop;",

                "CREATE TABLE IF NOT EXISTS customer"
                "(customer_id SERIAL, "
                "name VARCHAR(50), "
                "email VARCHAR(50),"
                "PRIMARY KEY (customer_id));",

                "CREATE TABLE IF NOT EXISTS publisher "
                "(publisher_id SERIAL,"
                "phone VARCHAR(20),"
                "address VARCHAR(255),"
                "PRIMARY KEY (publisher_id));",

                "CREATE TABLE IF NOT EXISTS book "
                "(book_id SERIAL,"
                "title VARCHAR(255),"
                "publisher_id BIGINT UNSIGNED,"
                "PRIMARY KEY (book_id),"
                "FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id));",

                "CREATE TABLE IF NOT EXISTS catalog "
                "(catalog_id SERIAL,"
                "book_id BIGINT UNSIGNED,"
                "shelf VARCHAR(255),"
                "PRIMARY KEY (catalog_id),"
                "FOREIGN KEY (book_id) REFERENCES book(book_id));",

                "CREATE TABLE IF NOT EXISTS checkout "
                "(checkout_id SERIAL,"
                "catalog_id BIGINT UNSIGNED,"
                "customer_id BIGINT UNSIGNED,"
                "checkout_date DATETIME,"
                "due_date DATETIME,"
                "PRIMARY KEY (checkout_id),"
                "FOREIGN KEY (catalog_id) REFERENCES catalog(catalog_id),"
                "FOREIGN KEY (customer_id) REFERENCES customer(customer_id));"]

timemanager_ddl = ["USE timemanager",

                   "CREATE TABLE IF NOT EXISTS employee"
                   "(employee_id SERIAL,"
                   "first_name VARCHAR(25),"
                   "last_name VARCHAR(25),"
                   "email VARCHAR(25),"
                   "PRIMARY KEY (employee_id));",

                   "CREATE TABLE IF NOT EXISTS project"
                   "(project_id SERIAL,"
                   "project_name VARCHAR(39),"
                   "description TEXT,"
                   "PRIMARY KEY (project_id));",

                   "CREATE TABLE IF NOT EXISTS time_entry"
                   "(time_entry_id SERIAL,"
                   "employee_id BIGINT UNSIGNED,"
                   "project_id BIGINT UNSIGNED,"
                   "date DATETIME,"
                   "hours_worked INT,"
                   "PRIMARY KEY (time_entry_id),"
                   "FOREIGN KEY (employee_id) REFERENCES employee(employee_id),"
                   "FOREIGN KEY (project_id) REFERENCES project(project_id));"]

cd_shop_ddl = ["USE cd_shop;",

               "CREATE TABLE IF NOT EXISTS artist"
               "(artist_id SERIAL,"
               "artist_name VARCHAR(59),"
               "PRIMARY KEY (artist_id));",

               "CREATE TABLE IF NOT EXISTS cd"
               "(cd_id SERIAL,"
               "cd_title VARCHAR(20),"
               "price DECIMAL(7,2),"
               "genre VARCHAR(20),"
               "artist_id bigint unsigned,"
               "PRIMARY KEY (cd_id),"
               "FOREIGN KEY (artist_id) REFERENCES artist(artist_id));",

               "CREATE TABLE IF NOT EXISTS track"
               "(track_id SERIAL,"
               "track_title VARCHAR(20),"
               "time INT,"
               "cd_id BIGINT UNSIGNED,"
               "PRIMARY KEY (track_id),"
               "FOREIGN KEY (cd_id) REFERENCES cd(cd_id));"]

create_db("bookshop", "timemanager", "cd_shop")

for element in (bookshop_ddl, timemanager_ddl, cd_shop_ddl):
    for sql_command in element:
        cursor.execute(sql_command)

