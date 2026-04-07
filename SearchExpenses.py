from amount import AmountEXP
from CategoryWise_ExpenseView import CategoryWise_ExpenseView
from Monthly_report import report
from YearlyEXP import YEARLY_report

class Expenses:
    def __init__(self):
        print("\n\n1. Category-Wise Expenses")
        print("2. Month-Wise Expenses")
        print("3. Year-Wise Expenses")
        print("4. Amount-Wise Expenses that lies in particular range") #problem
        print("5. to quit!!")
        k = int(input("Enter your choice (1-5): "))
        match(k):
            case 1:
               CategoryWise_ExpenseView() 
            case 2:
                report() 
            case 3:
                YEARLY_report()
            case 4:
                AmountEXP()
            case 5:
                quit       
            case _:
              print("Please Select Correct Choice")                                      
                                                                                            