import sys
from get_budget import current_budget, path


class AccountingGoods:
    total_budget = current_budget

    # def __init__(self):
    #     self.income = 0
    #     self.expenses = 0
    #     self.expense_list = []
    #     self.expense_name = []
    #     self.income_name = []
    #     self.income_list = []

    def add_expense(self, total_budget):
        expense = float(input('Enter your expense amount: $'))
        times_per_month = int(input('How many times per month: '))
        total_expense = expense * times_per_month
        if total_budget - total_expense >= 0:
            total_budget = total_budget - total_expense
            print(f'The expenses was accepted, your remaining budget is: ${total_budget}')
            return total_budget
        else:
            print('The expenses was rejected because the budget exceeded.')
            return total_budget

    def add_revenue(self, total_budget):
        revenue = float(input('Enter new monthly income: $'))
        total_budget = total_budget + revenue
        print(f'your new budget is: ${total_budget}')
        return total_budget

    def save_budget(self, total_budget):
        with open(path, 'w') as f:
            f.write(str(total_budget))
        f.close()

    def main(self):
        end_program = 'no'
        total_budget = current_budget
        while end_program == 'no':
            print('Welcome to the Accounting Goods Program')
            print('Menu Selections: ')
            print('1-Add an Expense: ')
            print('2-Add Revenue: ')
            print('3-Check Balance: ')
            print('4-Save progress')
            print('5-Exit without saving')

            choice = int(input('enter your selection: '))
            if choice == 1:
                total_budget = self.add_expense(total_budget)
            elif choice == 2:
                total_budget = self.add_revenue(total_budget)
            elif choice == 3:
                print(f'Your balance is {total_budget}')
            elif choice == 4:
                self.save_budget(total_budget)
                print('Thanks for saving your progress')
            elif choice == 5:
                end_program = 'yes'
                print('Thank you for using "Accounting Goods" program, Goodbye')
            else:
                print('Invalid selection, please try again')


if __name__ == '__main__':
    AccountingGoods()
