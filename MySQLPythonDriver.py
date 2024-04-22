import mysql.connector
from mysql.connector import Error

def connect_fetch():
    try:
        # Connection parameters
        conn = mysql.connector.connect(
            host='localhost',        # Or the appropriate host where your database is hosted
            database='DevEnviroTests',
            user='root',    # Replace with your MySQL database username
            password='Root123456' # Replace with your MySQL database password
        )
        if conn.is_connected():
            print('Connected to the database')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            # Fetch all the rows from the last executed query
            rows = cursor.fetchall()
            print('Total Row(s):', cursor.rowcount)       
            # Print the rows
            for row in rows:
                print(row)        
            cursor.close()
    except Error as e:
        print('Error:', e)
    finally:
        if conn is not 'connected':
            conn.close()
            print('Database connection closed.')



def insert_user(user_data):
    """ Insert a new user into the Users table """
    query = "INSERT INTO Users(id, name, pass) VALUES (%s, %s, %s)"
    try:
        conn = mysql.connector.connect(
            host='localhost',        # Or the appropriate host where your database is hosted
            database='DevEnviroTests',
            user='root',    # Replace with your MySQL database username
            password='Root123456' # Replace with your MySQL database password
        )
        if conn.is_connected():
            cursor = conn.cursor()
            # Executing the SQL command
            cursor.execute(query, user_data)
            
            # Commit your changes in the database
            conn.commit()
            print("User inserted successfully.")

    except Error as e:
        print("Error while connecting to MySQL", e)
        # Rollback in case there is any error
        conn.rollback()

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def main():
    # Data to be inserted
    id = 3333
    name= 'John Doe'
    password='johndoe123'
    user_data = (id, name, password)  # Example data
    insert_user(user_data)

def mainEncrypted():
    # Data to be inserted
    id = 11111
    name= 'John Doe'
    key='O5/B0r4Dr1TWxpjF5V5Ba82aXBR1vTUPZwRR+huvbFQ='
    password='johndoe123'
    user_data = (id, name, password)  # Example data
    insert_user(user_data)


if __name__ == '__main__':
    main()
    connect_fetch()
    
