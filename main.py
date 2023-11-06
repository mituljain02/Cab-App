# import setup_checks
# import insertdata
# import userfunctions
# import others


# # Connect to the database
# result = setup_checks.connect_to_database()

# if result is None:
#     print("Error connecting to database")
# else:
#     connection, cursor = result
#     print("Connected to database successfully")

#     # Create table
#     setup_checks.create_table(connection, cursor, "Cab_Details")

#     # Insert data into the table
# insertdata.insert_data(connection, cursor)


# while True:
#     others.menu()
#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         userfunctions.book_cab(connection, cursor)
#     elif choice == 2:
#         userfunctions.cancel_booking(connection, cursor)
#     elif choice == 3:
#         userfunctions.check_fares(connection, cursor)
#     elif choice == 4:
#         userfunctions.show_bookings(connection, cursor)
#     elif choice == 5:
#         userfunctions.show_available_cab(connection, cursor)
#     elif choice == 6:
#         others.clear_screen()
#     elif choice == 7:
#         others.about()
#     elif choice == 8:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# # Close cursor and connection
# cursor.close()
# connection.close()
import setup_checks
import insertdata
import userfunctions
import others

# Connect to the database
result = setup_checks.connect_to_database()

if result is None:
    print("Error connecting to database")
else:
    connection, cursor = result
    print("Connected to database successfully")

    # Create table
    setup_checks.create_table(connection, cursor, "Cab_Details")

    # Insert data into the table
    insertdata.insert_data(connection, cursor)

    # Create an instance of the Cab class
    cab = userfunctions.Cab(connection, cursor)

    while True:
        others.menu()
        choice = int(input("Enter choice: "))

        if choice == 1:
            cab.book_cab()
        elif choice == 2:
            cab.cancel_booking()
        elif choice == 3:
            cab.check_fares(cursor)
        elif choice == 4:
            cab.show_bookings()
        elif choice == 5:
            cab.show_available_cab()
        elif choice == 6:
            others.clear_screen()
        elif choice == 7:
            others.about()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Close cursor and connection
cursor.close()
connection.close()
