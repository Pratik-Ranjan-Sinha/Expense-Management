class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount) 
        self.category = category
        self.date = date
        self.description = description 

    @classmethod
    def from_input(cls):
        amount = input("Enter Amount: ")
        category = input("Enter category (Food/Transport/Entertainment/Shopping/Other): ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        return cls(amount, category, date, description)
    # def Amounts(self):
    #     self.__amount = float(input("Enter Amount: "))

    # def Categories(self):
    #     self.__category = input("Enter category (Food/Transport/Entertainment/Shopping/Other): ")

    # def Dates(self):
    #     self.__date = input("Enter date (YYYY-MM-DD): ")

    # def Descriptions(self):
    #     self.__description = input("Enter description: ")

    def __str__(self):
        return f"{self.amount}, {self.category}, {self.date}, {self.description}"


# exp = Expense(
#     input("Enter Amount: "), 
#     input("Enter category (Food/Transport/Entertainment/Shopping/Other): "), 
#     input("Enter date (YYYY-MM-DD): "), 
#     input("Enter description: ")
# )
# # exp.Amounts()
# # exp.Categories()
# # exp.Dates()
# # exp.Descriptions()
# print("✅ Expense added successfully!")