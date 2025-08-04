import pandas as pd
from datetime import datetime

class BudgetAgent:
    def __init__(self, data_path='data/transactions.csv'):
        self.data_path = data_path
        try:
            self.df = pd.read_csv(self.data_path)
        except:
            self.df = pd.DataFrame(columns=["Date", "Type", "Category", "Amount"])
            self.df.to_csv(self.data_path, index=False)

    def add_transaction(self, trans_type, category, amount):
        new_row = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Type": trans_type,
            "Category": category,
            "Amount": amount
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.data_path, index=False)

    def get_summary(self):
        if self.df.empty:
            return None
        income = self.df[self.df['Type'] == 'Income']['Amount'].sum()
        expense = self.df[self.df['Type'] == 'Expense']['Amount'].sum()
        balance = income - expense
        return income, expense, balance

    def get_category_breakdown(self):
        if self.df.empty:
            return pd.DataFrame()
        expense_data = self.df[self.df['Type'] == 'Expense']
        return expense_data.groupby('Category')['Amount'].sum().reset_index()
