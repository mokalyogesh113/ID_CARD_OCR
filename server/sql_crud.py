# Libraries
import mysql.connector
from flask import jsonify

# Created the connection 
mydb = mysql.connector.connect(
host="localhost",
port = 3306,
user="root",
password="Netwin@123",
database="ycm_db" ,
charset='utf8'
)



def insert_pan_data(data):
    try:
        # Create a cursor object
        mycursor = mydb.cursor()

        # Initialize variables
        pan_no = data.get('pan_no', '')
        name = data.get('name', '')
        father_name = data.get('father_name', '')
        dob = data.get('dob', '')

        # Execute the insert query
        insert_query = "INSERT INTO pan_data (pan_no, name, father_name, dob) VALUES (%s, %s, %s, %s)"
        mycursor.execute(insert_query, (pan_no, name, father_name, dob))

        # Commit the transaction
        mydb.commit()

        print("Data inserted successfully")
        return True

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        if mycursor:
            mycursor.close()


def get_pan_data(id=None):
    try:
        
        # Create a cursor object
        mycursor = mydb.cursor(dictionary=True)

        if id is not None:
            # Query to retrieve data for a specific ID
            query = "SELECT * FROM pan_data WHERE id = %s"
            mycursor.execute(query, (id,))
        else:
            # Query to retrieve all data
            query = "SELECT * FROM pan_data"
            mycursor.execute(query)

        # Fetch all rows
        rows = mycursor.fetchall()

        # Close cursor and database connection
        mycursor.close()

        # Return the result in JSON format
        return jsonify(rows)

    except mysql.connector.Error as err:
        print("Error:", err)
        return jsonify({"error": "Failed to fetch data"})




if __name__ == '__main__':
    print(mydb)
    insert_pan_data('1')







'''
pip install mysql-connector-python
'''