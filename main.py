from file_manager import fileManager

def Header():
    for i in range(50):
        print("=", end="")
    print("\n\tPersonal Finance Manager")
    for i in range(50):
        print("=", end="")

def mainMenu():
    print("\n\n1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Category-wise Summary")
    print("4. Generate Monthly Report")
    print("5. Search Expenses")
    print("6. Backup Data")
    print("7. Exit")
    k = int(input("Enter your choice (1-7): "))

    match(k):
        case 1:
            fileManager() # Class of file_manager.py
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            quit
        case _:
            print("Please Select Correct Choice")

Header()
mainMenu()