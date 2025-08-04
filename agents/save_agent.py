class SaveAgent:
    def __init__(self, income, expense):
        self.income = income
        self.expense = expense
        self.balance = income - expense

    def calculate_saving_advice(self):
        if self.income == 0:
            return "❗ No income recorded yet. Cannot suggest savings."

        saving_percent = (self.balance / self.income) * 100

        if saving_percent > 30:
            return f"✅ Great! You're saving {saving_percent:.1f}% of your income. Keep it up!"
        elif 10 <= saving_percent <= 30:
            return f"👍 You're saving {saving_percent:.1f}% of your income. Try to save more if possible."
        elif saving_percent > 0:
            return f"⚠️ Low savings: {saving_percent:.1f}%. Reduce expenses to improve savings."
        else:
            return "🚨 You're spending more than you earn! Review your expenses immediately."
