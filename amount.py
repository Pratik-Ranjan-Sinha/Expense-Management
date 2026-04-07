import csv

class AmountEXP():
    def __init__(self):    
        file =open("data/expense.csv", "r")
        reader = csv.reader(file)
        # print(reader)
        min_amount = float(input("Enter minimum amount: "))
        max_amount = float(input("Enter maximum amount: "))
        print("=" * 50)
        print("\tAmount-Wise Expenses")
        print("=" * 50)
        next(reader)
        for row in reader:
            # print(type(row[0]))
            amount = float(row[0])
            if amount >= min_amount and amount <= max_amount:
                print("\nAmount:", row[0])
                print("Category:", row[1])
                print("Date:", row[2])
                print("Description:", row[3])
                print("-"*20)  
        file.close()

# AmountEXP()