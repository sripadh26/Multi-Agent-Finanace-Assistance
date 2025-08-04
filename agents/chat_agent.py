from textblob import TextBlob
import pandas as pd

class ChatAgent:
    def __init__(self, budget_agent, spending_agent):
        self.budget_agent = budget_agent
        self.spending_agent = spending_agent
        self.df = pd.read_csv(self.budget_agent.data_path)

    def answer_query(self, query):
        query = query.lower()
        blob = TextBlob(query)

        if "balance" in query or "how much money" in query:
            income, expense, balance = self.budget_agent.get_summary()
            return f"Your current balance is ₹{balance:.2f}"

        elif "total income" in query:
            income, _, _ = self.budget_agent.get_summary()
            return f"Your total income is ₹{income:.2f}"

        elif "total expense" in query or "total spent" in query:
            _, expense, _ = self.budget_agent.get_summary()
            return f"Your total expenses are ₹{expense:.2f}"

        elif "how much did i spend on" in query:
            category = query.split("on")[-1].strip().capitalize()
            filtered = self.df[(self.df['Type'] == 'Expense') & (self.df['Category'] == category)]
            if not filtered.empty:
                total = filtered['Amount'].sum()
                return f"You spent ₹{total:.2f} on {category}."
            else:
                return f"No spending data found for '{category}'."

        elif "top" in query and "spending" in query:
            top_cats = self.spending_agent.get_top_categories()
            if not top_cats.empty:
                result = "Top spending categories:\n"
                for i, row in top_cats.iterrows():
                    result += f"- {row['Category']}: ₹{row['Amount']:.2f}\n"
                return result
            else:
                return "No expenses recorded yet."

        else:
            return "Sorry, I couldn't understand that. Try asking about balance, income, or category-wise expenses."
