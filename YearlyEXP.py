import csv

class YEARLY_report:
    def __init__(self):
        year= int(input("Enter the year  "))

        print("=" * 50)
        print("\tYearly Report")
        print("=" * 50)

        file = open("data/expense.csv", "r")
        reader = csv.reader(file)

        next(reader)

        found = False
        for row in reader:
            y = row[2]
            m = int(y[0:4])

            if m == year:
                found = True
                print("\nAmount:", row[0])
                print("Category:", row[1])
                print("Date:", row[2])
                print("Description:", row[3])
                print("-" * 24)

        file.close()

        if not found:
            print("No expenses found for this month.")