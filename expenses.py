import uuid
from datetime import datetime,timezone

#Expense class - Represents an individual financial expense.

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4()) 
        self.title = title
        self.amount = amount
        self.created_at  = datetime.utcnow()
        self.updated_at = self.created_at


    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    

# ExpenseDatabase class - Manages a collection of Expense objects.
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, expense_title):
        expenses_result = []
        for expense in self.expenses:
            if expense.expense_title == expense_title:
                expenses_result.append(expense)
        return expenses_result
        
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
