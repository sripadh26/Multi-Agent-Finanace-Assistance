class InvestAgent:
    def __init__(self, income, expense):
        self.income = income
        self.expense = expense
        self.savings = income - expense

    def suggest_investment(self):
        if self.income == 0:
            return "❗ No income recorded. Unable to suggest investments."

        if self.savings <= 0:
            return "🚨 You have no savings this month. Try reducing expenses."

        suggestions = []

        if self.savings >= 10000:
            suggestions.append("📌 Consider starting a **SIP** in Index Funds or Mutual Funds.")
            suggestions.append("📌 Try investing in a **Public Provident Fund (PPF)**.")
        elif self.savings >= 5000:
            suggestions.append("📌 Start a **Recurring Deposit (RD)** in your bank.")
            suggestions.append("📌 Try a **low-risk Mutual Fund SIP**.")
        elif self.savings >= 1000:
            suggestions.append("📌 Use a **Digital Gold savings plan**.")
            suggestions.append("📌 Keep the rest in a **high-interest savings account**.")
        else:
            suggestions.append("💡 Try to save a bit more to start investing meaningfully.")

        suggestions.append("✅ Always keep an emergency fund equal to 2–3 months of expenses.")

        return "\n\n".join(suggestions)
