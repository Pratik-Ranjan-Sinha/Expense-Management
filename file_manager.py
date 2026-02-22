from expense import Expense
import csv # built-in Module
from datetime import datetime

exp = Expense.from_input()
# exp = Expense(
#     input("Enter Amount: "), 
#     input("Enter category (Food/Transport/Entertainment/Shopping/Other): "), 
#     input("Enter date (YYYY-MM-DD): "), 
#     input("Enter description: ")
# )

# adding data to the expense.csv file
file = open('data/expense.csv','a', newline='')
writer = csv.writer(file)

# Add the Exeption Handeling to this code.
if exp.amount > 0:
    if exp.category == "Food" or exp.category =="Transport" or exp.category =="Entertainment" or exp.category =="Shopping" or exp.category =="Other":
        try: 
            valid_date = datetime.strptime(exp.date, "%Y-%m-%d")
            writer.writerow([
                exp.amount, 
                exp.category,
                exp.date, 
                exp.description
            ])
        except ValueError:
            raise ValueError("Invalid Date Format")
    else:
        raise ValueError("Please select the Correct Option")
else:
    raise ValueError("Amount should be greater than 0")
file.close

# to fetch the data use this one
# with open('data/expense.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ')
#     for row in spamreader:
#         print(', '.join(row))

print("✅ Expense added successfully!")