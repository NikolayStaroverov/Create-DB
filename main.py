import psycopg2

conn=psycopg2.connect(database="test_db", user="postgres", password="Snicks")


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute(""
                    "DROP TABLE IF EXISTS PHONE_DB; DROP TABLE IF EXISTS CLIENTS_NAME;""")

        cur.execute("CREATE TABLE IF NOT EXISTS CLIENTS_NAME ("
                    "ID SERIAL PRIMARY KEY ,"
                    "NAME VARCHAR (20) NOT NULL, "
                    "SURNAME VARCHAR (20) NOT NULL,"
                    "EMAIL VARCHAR (20) NOT NULL);")

        cur.execute("CREATE TABLE IF NOT EXISTS PHONE_DB ("
                    "ID SERIAL PRIMARY KEY,"
                    "CLIENT_ID INTEGER NOT NULL REFERENCES CLIENTS_NAME (ID), "
                    "PHONE VARCHAR (10) NOT NULL);")

        conn.commit()

def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO CLIENTS_NAME (NAME,SURNAME,EMAIL) "
                    "values (%s,%s,%s) "
                    "returning ID,NAME, SURNAME, EMAIL;", (first_name, last_name, email))
        print(cur.fetchone())

def add_phone(conn,client_id, phone):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO PHONE_DB (CLIENT_ID,PHONE) "
                    "values (%s,%s) "
                    "returning ID,PHONE;", (client_id, phone))
        print(cur.fetchone())


def change_client(conn, client_id, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute("UPDATE CLIENTS_NAME set NAME=%s where ID=%s RETURNING NAME,SURNAME,EMAIL,ID;", (first_name, client_id))
        cur.execute("UPDATE CLIENTS_NAME set SURNAME=%s where ID=%s RETURNING NAME,SURNAME,EMAIL,ID;", (last_name, client_id))
        cur.execute("UPDATE CLIENTS_NAME set EMAIL=%s where ID=%s RETURNING NAME,SURNAME,EMAIL,ID;", (email, client_id))
        print(cur.fetchall())


def delete_phone(conn,client_id, phone):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM PHONE_DB where CLIENT_ID=%s and PHONE=%s RETURNING ID,CLIENT_ID,PHONE ;",(client_id,phone))
        print(cur.fetchall())

def delete_client (conn, client_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM CLIENTS_NAME where ID=%s;",(client_id,))
        conn.commit()


def find_client(cur, first_name, last_name, email, phone):
    with conn.cursor() as cur:
      cur.execute("""
        SELECT CLIENTS_NAME.NAME, CLIENTS_NAME.SURNAME, CLIENTS_NAME.EMAIL, PHONE_DB.PHONE FROM CLIENTS_NAME 
        LEFT JOIN PHONE_DB 
        ON PHONE_DB.CLIENT_ID=CLIENTS_NAME.ID
        WHERE CLIENTS_NAME.NAME=%s 
        AND CLIENTS_NAME.SURNAME=%s      
        AND CLIENTS_NAME.EMAIL=%s 
        AND PHONE_DB.PHONE=%s;
        """, (first_name, last_name, email, phone, ))
      print(cur.fetchall())
      return cur.fetchall()


with psycopg2.connect(database="test_db", user="postgres", password="Snicks") as conn:
    create_db(conn)

    add_client(conn,"Ivan_1", "Ivanov_1", "ivanov_1@mail.ru")
    add_client(conn,"Ivan_2", "Ivanov_2", "ivanov_2@mail.ru")
    add_client(conn, "Ivan_3", "Ivanov_3", "ivanov_3@mail.ru")

    add_phone(conn,1,"1_12345678")
    add_phone(conn,2,"2_12345678")
    add_phone(conn, 3, "3_12345678")

    change_client(conn,1,"Petr","Petrov","petrov@mail.ru")
    delete_phone (conn,2,"2_12345678")
    delete_client(conn,2)
    find_client (conn,"Ivan_1","Ivanov_1","ivanov_1@mail.ru","1_12345678")

conn.close