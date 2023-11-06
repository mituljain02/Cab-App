from abc import ABC,abstractmethod
import mysql.connector


class book(ABC):
    @abstractmethod
    def book_cab():
        return 0


class Cab:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def book_cab(self):
        try:
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            self.cursor.execute("Select * from cab_details where Source_Station_Name = %s AND Destination_Station_Name = %s", (source, destination))
            result = self.cursor.fetchall()
            if result:
                for row in result:
                    print("Cab No: ", row[0])
                    print("Source: ", row[6], " - ", row[7])
                    print("Destination: ", row[8], " - ", row[9])
                    print("Approximate Arrival Time: ", row[3])
                    self.cursor.execute("Update cab_details SET cab_booked = 1 where Source_Station_Name = %s AND Destination_Station_Name = %s", (source, destination))
                    self.connection.commit()
            else:
                print("No cabs available for the given source and destination.")
        except mysql.connector.Error as e_error:
            print("Error booking cab: ", e_error)

    def cancel_booking(self):
        try:
            Cab_No = input("Enter cab number to be cancelled: ")
            self.cursor.execute("Update Cab_Details SET cab_booked = 0 WHERE Cab_No = %s", (Cab_No,))
            self.connection.commit()
            print("Booking cancelled successfully.")
        except mysql.connector.Error as e_error:
            print("Error cancelling booking: ", e_error)

    @staticmethod
    def check_fares(cursor):
        try:
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            cursor.execute("SELECT Distance_In_Kms FROM Cab_Details WHERE Source_Station_Name = %s AND Destination_Station_Name = %s", (source, destination))
            result = cursor.fetchall()
            if result:
                for row in result:
                    print("Fare for the distance of ", row[0], " kms is: $", (row[0] * 5))
            else:
                print("Fare information not available for the given source and destination.")
        except mysql.connector.Error as e_error:
            print("Error checking fares: ", e_error)

    def show_bookings(self):
        try:
            self.cursor.execute("SELECT * FROM Cab_Details WHERE cab_booked = 1")
            result = self.cursor.fetchall()
            if result:
                for row in result:
                    print("Cab No: ", row[0])
                    print("Source: ", row[6], " - ", row[7])
                    print("Destination: ", row[8], " - ", row[9])
                    print("Approximate Arrival Time: ", row[3])
                    print("Approximate Departure Time: ", row[4])
                    print("Distance: ", row[5], " kms")
                    print("----------------------------")
            else:
                print("No cabs available.")
        except mysql.connector.Error as e_error:
            print("Error showing available cabs: ", e_error)

    def show_available_cab(self):
        try:
            self.cursor.execute("SELECT * FROM Cab_Details where cab_booked = 0")
            result = self.cursor.fetchall()
            if result:
                for row in result:
                    print("Cab No: ", row[0])
                    print("Source: ", row[6], " - ", row[7])
                    print("Destination: ", row[8], " - ", row[9])
                    print("Approximate Arrival Time: ", row[3])
                    print("Approximate Departure Time: ", row[4])
                    print("Distance: ", row[5], " kms")
                    print("----------------------------")
            else:
                print("No cabs available.")
        except mysql.connector.Error as e_error:
            print("Error showing available cabs: ", e_error)
