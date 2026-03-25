import csv

class ViewExpense:
     def __init__(self):
        try:
             file = open("data/expense.csv", "r")
             reader = csv.reader(file)
             for i in range(50):
                 print("=", end="")
             print("\n\tAll The Expenses")
             for i in range(50):
                 print("=", end="")
             
             for row in reader:
                  print("\nAmount:", row[0])
                  print("Category:", row[1])
                  print("Date:", row[2])
                  print("Description:", row[3])
                  print("----------------------")
             file.close()

        except:
            print("File not found or error occurred")        


