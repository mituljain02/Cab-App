# Clear Screen
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu
def menu():
    print("Welcome to Travel Planner")
    print("Please select an option: ")
    print("1. Book a Cab")
    print("2. Cancel a Booking")
    print("3. Check Fares")
    print("4. Show my Bookings")
    print("5. Show Available Cabs")
    print("6. Clear Screen")
    print("7. About")
    print("8. Exit")

# About
def about():
    with open(__file__, 'r') as f:
        print(f.read())
