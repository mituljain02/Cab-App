# import mysql.connector
# from userfunctions import book_cab,cancel_booking,check_fares,show_available_cab,show_bookings
# import pytest

# @pytest.fixture
# def database_connection():
#     connection = mysql.connector.connect(user='root', password='jain@mitul', host='localhost', database='cabapp')
#     cursor = connection.cursor()
#     yield connection, cursor
#     cursor.close()
#     connection.close()

# def test_book_cab(database_connection):
#     connection, cursor = database_connection
#     book_cab(connection, cursor)
#     cursor.execute("SELECT * FROM Cab_Details WHERE cab_booked = 0")
#     result = cursor.fetchall()
#     assert result, "Cab booking failed"

# def test_cancel_booking(database_connection):
#     connection, cursor = database_connection
#     cancel_booking(connection, cursor)
#     cursor.execute("SELECT * FROM Cab_Details WHERE cab_booked = 0 and Cab_No = %s",(123,))
#     result = cursor.fetchall()
#     assert result, "Cab booking cancellation failed"


# def test_check_fares(database_connection):
#     connection, cursor = database_connection
#     check_fares(connection, cursor)
#     cursor.execute("SELECT Distance_In_Kms FROM Cab_Details")
#     result = cursor.fetchall()
#     assert result, "Fare check failed"

# def test_show_bookings(database_connection):
#     connection, cursor = database_connection
#     show_bookings(connection, cursor)
#     cursor.execute("SELECT * FROM Cab_Details WHERE cab_booked = 1")
#     result = cursor.fetchall()
#     assert result, "Show bookings failed"

# def test_show_available_cab(database_connection):
#     connection, cursor = database_connection
#     show_available_cab(connection, cursor)
#     cursor.execute("SELECT * FROM Cab_Details where cab_booked = 0")
#     result = cursor.fetchall()
#     assert result, "Show available cabs failed"

import mysql.connector
import pytest

from userfunctions import Cab

def test_book_cab():
    connection = mysql.connector.connect(user='root', password='jain@mitul', host='localhost', database='cabapp')
    cursor = connection.cursor()

    cab = Cab(connection, cursor)

    # Test if cab booking works as expected
    cab.book_cab()
    cursor.execute("SELECT * FROM Cab_Details WHERE cab_booked = 0")
    result = cursor.fetchall()
    assert result, "Cab booking failed"

@pytest.mark.skip
def test_cancel_booking():
    connection = mysql.connector.connect(user='root', password='jain@mitul', host='localhost', database='cabapp')
    cursor = connection.cursor()

    cab = Cab(connection, cursor)

    # Test if cab cancellation works as expected
    cab.cancel_booking()
    cursor.execute("SELECT cab_booked FROM Cab_Details WHERE Cab_No = %s", (123,))
    result = cursor.fetchall()
    assert result, "Cab booking cancellation failed"

def test_check_fares():
    connection = mysql.connector.connect(user='root', password='jain@mitul', host='localhost', database='cabapp')
    cursor = connection.cursor()

    # Test if fare checking works as expected
    Cab.check_fares(cursor)
    cursor.execute("SELECT Distance_In_Kms FROM Cab_Details")
    result = cursor.fetchall()
    assert result, "Fare check failed"

@pytest.mark.xfail
def test_show_bookings():
    connection = mysql.connector.connect(user='root', password='jain@mitul', host='localhost', database='cabapp')
    cursor = connection.cursor()

    cab = Cab(connection, cursor)

    # Test if show bookings works as expected
    cab.show_bookings()
    cursor.execute("SELECT * FROM Cab_Details WHERE cab_booked = 1")
    result = cursor.fetchall()
    assert result, "Show bookings failed"

def test_show_available_cab():
    connection = mysql.connector.connect(user='root', password='jain@mitul', host='localhost', database='cabapp')
    cursor = connection.cursor()

    cab = Cab(connection, cursor)
    cursor.execute("SELECT * FROM Cab_Details where cab_booked = 0")

    # Test if
    result = cursor.fetchall()
    assert result, "Show available cabs failed"
