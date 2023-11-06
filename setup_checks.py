import mysql.connector
# importing mysql.connector to make a database connection


def connect_to_database():
    # Connect to the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jain@mitul",
            database="cabapp"
        )
        cursor = connection.cursor()
        print("Connected to database successfully")
        return connection, cursor
    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)


def create_table(connection, cursor, table_name):
    # Create the Cab Details table
    query = '''CREATE TABLE IF NOT EXISTS Cab_Details (
                Cab_No INT PRIMARY KEY,
                Station_Code VARCHAR(10),
                Station_Name VARCHAR(255),
                Approx_Arrival_Time DATETIME,
                Approx_Departure_Time DATETIME,
                Distance_in_Kms FLOAT,
                Source_Station VARCHAR(10),
                Source_Station_Name VARCHAR(255),
                Destination_Station VARCHAR(10),
                Destination_Station_Name VARCHAR(255)
            );'''
    cursor.execute(query)
    connection.commit()

class Checks:
    pass
