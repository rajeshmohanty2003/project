import time

def automatic_mode():
    red_time = int(input("Enter Red light time (seconds): "))
    yellow_time = int(input("Enter Yellow light time (seconds): "))
    green_time = int(input("Enter Green light time (seconds): "))

    while True:
        print("\nRED Light - STOP")
        time.sleep(red_time)

        print("YELLOW Light - READY")
        time.sleep(yellow_time)

        print("GREEN Light - GO")
        time.sleep(green_time)

        ch = input("\nDo you want to continue in automatic mode? (y/n): ")
        if ch.lower() != 'y':
            break

def manual_mode():
    while True:
        print("\n1. RED Light")
        print("2. YELLOW Light")
        print("3. GREEN Light")
        print("4. Exit Manual Mode")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("RED Light - STOP")
        elif choice == "2":
            print("YELLOW Light - READY")
        elif choice == "3":
            print("GREEN Light - GO")
        elif choice == "4":
            break
        else:
            print("Galat choice")

while True:
    print("\nTraffic Light Control System")
    print("1. Automatic Mode")
    print("2. Manual Mode")
    print("3. Exit")

    option = input("Select an option: ")

    if option == "1":
        automatic_mode()
    elif option == "2":
        manual_mode()
    elif option == "3":
        print("System exited successfully")
        break
    else:
        print("Invalid option")