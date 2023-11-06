import mysql.connector

def insert_data(connection, cursor):
    try:
        cab_no = input("Enter cab number: ")
        station_code = input("Enter station code: ")
        station_name = input("Enter station name: ")
        approx_arrival_time = input("Enter approx arrival time: ")
        approx_departure_time = input("Enter approx departure time: ")
        distance_in_kms = input("Enter distance in kms: ")
        source_station = input("Enter source station: ")
        source_station_name = input("Enter source station name: ")
        destination_station = input("Enter destination station: ")
        destination_station_name = input("Enter destination station name: ")

        cursor.execute("INSERT INTO Cab_Details (Cab_No, Station_Code, Station_Name, Approx_Arrival_Time, Approx_Departure_Time, Distance_In_Kms, Source_Station, Source_Station_Name, Destination_Station, Destination_Station_Name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (cab_no, station_code, station_name, approx_arrival_time, approx_departure_time, distance_in_kms, source_station, source_station_name, destination_station, destination_station_name))
        connection.commit()
        print("Data inserted successfully.")
    except Error as e_error:
        print("Error inserting data: ", e_error)
