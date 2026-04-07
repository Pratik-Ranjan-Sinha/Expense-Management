import csv

class CategoryWise_ExpenseView:
    def __init__(self):
        try:
            file = open("data/expense.csv", "r")
            reader = csv.reader(file)
            for i in range(50):
                print("=", end="")
            print("\n\tCategory-wise Summary")         
            for i in range(50):
                print("=", end="")
            
            Category=input("\nEnter your category to be viewed(Food/Transport/Entertainment/Shopping/Other): ")
            if Category=="Food" or Category=="Transport" or Category=="Entertainment" or Category=="Shopping" or Category=="Other":
                for row in reader:
                    c=row[1]
                    if Category==c:
                        print("\nAmount:", row[0])
                        print("Category:", row[1])
                        print("Date:", row[2])
                        print("Description:", row[3])
                        print("----------------------")
                file.close() 
            else:
                raise ValueError("Category not found")         
        except:
            print("File not found or error occurred")                 
                  
