import sys
from get_budget import current_budget, path


class AccountingGoods:
    total_budget = current_budget

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.expense_list = []
        self.expense_name = []
        self.income_name = []
        self.income_list = []
        self.prompt_income()

    def income_ask(self):
        add_income = input('Add income? [y/n]: ')
        return add_income

    # def save_ask(self):
    #     ask_save_progress = input('save progress? [y/n]: ')
    #     return ask_save_progress

    def income_sum(self):
        self.income = sum(self.income_list)

    def expense_ask(self):
        add_expense = input('Add expense? [y/n]: ')
        return add_expense

    def month_revenue(self, total_budget):
        revenue = float(input('Enter new monthly income: $'))
        self.total_budget = total_budget + revenue
        print(f'your new budget is: ${total_budget}')
        return self.total_budget

    def week_revenue(self, total_budget):
        revenue = float(input('Enter new week income: $'))
        self.total_budget = total_budget + revenue
        print(f'your new budget is: ${total_budget}')
        return self.total_budget

    def day_revenue(self, total_budget):
        revenue = float(input('Enter new day income: $'))
        self.total_budget = total_budget + revenue
        print(f'your new budget is: ${total_budget}')
        return self.total_budget

    def expense_sum(self):
        self.expenses = sum(self.expense_list)

    def income_check(self):
        if not self.income_list:
            print('Please enter at least one source of income. ')
            self.prompt_income()
        else:
            return

    def expense_check(self):
        if not self.expense_list:
            print('Please enter at least one expense. ')
            self.prompt_expense()
        else:
            return

    def prompt_income(self):
        x = False
        while not x:
            result = self.income_ask()
            if result == 'y':
                income_input = float(input('Enter source of income. [Numbers Only]: '))
                self.income_list.append(income_input)
                income_name = input('Enter income name. [Name Only]: ')
                self.income_name.append(income_name)
            else:
                self.income_check()
                x = True
        self.income_sum()
        name = [name for name in self.income_name]
        income = [income for income in self.income_list]
        income_dict = dict(zip(name, income))
        for k in income_dict:
            print(k + ': ', '$' + str(income_dict[k]))
        print('Total user income: ', '$' + str(self.income))
        self.prompt_expense()

    def prompt_expense(self):
        x = False
        while not x:
            result = self.expense_ask()
            if result == 'y':
                expense_input = float(input('Enter expense amount. [Numbers Only]: '))
                self.expense_list.append(expense_input)
                expense_name = input('Enter expense name. [Name Only]: ')
                self.expense_name.append(expense_name)
            else:
                self.expense_check()
                x = True
        self.expense_sum()
        name = [name for name in self.expense_name]
        expense = [income for income in self.expense_list]
        expense_dict = dict(zip(name, expense))
        for k in expense_dict:
            print(k + ': ', '$' + str(expense_dict[k]))
        print('Total user expenses: ', '$' + str(self.expenses))
        self.user_value()

    def user_value(self):
        val_output = self.income - self.expenses
        if val_output < 0:
            print('You are in the negative, you have a deficit of ' + '$' + str(val_output))
        if val_output == 0:
            print('You have broken even, you are spending exactly as much as you make.')
        if val_output > 0:
            print('You are in the positive, you have a surplus of ' + '$' + str(val_output))
        another = input('Do you want to save the result? [y/n]: ')
        if another == 'y':
            self.save_result(self.total_budget)
        else:
            self.close_program()

    def save_result(self, total_budget):
        with open(path, 'w') as f:
            f.write(str(total_budget))
        f.close()

    def close_program(self):
        print('Exiting Program.')
        sys.exit(0)