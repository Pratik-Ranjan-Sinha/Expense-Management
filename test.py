from datetime import datetime

date = input("Enter date (yyyy-mm-dd): ")

if date == datetime.strptime(date, "%y-%m-%d"):
    print("yes it is")
else:
    print("no it is not")

# from datetime import datetime

# date_input = input("Enter date (yyyy-mm-dd): ")

# try:
#     # Try converting the string into a date object
#     valid_date = datetime.strptime(date_input, "%Y-%m-%d")
#     print("Valid date entered ✅")
    
# except ValueError:
#     print("Invalid format ❌ Please enter date in yyyy-mm-dd format")