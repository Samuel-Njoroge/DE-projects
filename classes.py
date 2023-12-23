import uuid
from datetime import datetime, timezone

# Expense class
class Expense:
    def __init__(self, id, title, amount, created_at, updated_at):
        self.id = id
        self.title = title
        self.amount = amount
        self.created_at  = created_at
        self.updated_at = updated_at


    def update(self, title=None, amount=None):
        expense = []
        expense.append()

    def to_dict(self):
        return dict()
    

# ExpenseDatabase class
class ExpenseDatabase:
    def __init__(self, expenses, expense_id, expense_title):
        self.expenses = expenses
        self.expense_id = expense_id
        self.expense_title = expense_title
        expenses = []

    def add_expense(self, expense):
        expenses.append(expense)

    def remove_expense(self, expense_id):
        pass

    def get_expense_by_id(self, expense_id):

    def get_expense_by_title(self, expense_title)
        
    def to_dict(self):
