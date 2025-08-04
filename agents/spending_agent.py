import pandas as pd

class SpendingAgent:
    def __init__(self, data_path='data/transactions.csv'):
        self.data_path = data_path
        try:
            self.df = pd.read_csv(self.data_path)
        except:
            self.df = pd.DataFrame(columns=["Date", "Type", "Category", "Amount"])

    def get_top_categories(self, top_n=5):
        expense_data = self.df[self.df['Type'] == 'Expense']
        if expense_data.empty:
            return pd.DataFrame()
        return expense_data.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(top_n).reset_index()

    def get_alerts(self, limits=None):
        """
        limits = {
            'Food': 5000,
            'Shopping': 3000
        }
        """
        if limits is None:
            limits = {
                'Food': 5000,
                'Shopping': 3000,
                'Entertainment': 2000,
                'Travel': 4000,
            }

        alerts = []
        expense_data = self.df[self.df['Type'] == 'Expense']
        total_per_category = expense_data.groupby("Category")["Amount"].sum()

        for category, total in total_per_category.items():
            if category in limits and total > limits[category]:
                alerts.append((category, total, limits[category]))

        return alerts
