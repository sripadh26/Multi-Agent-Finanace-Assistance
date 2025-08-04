# app.py

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from agents.budget_agent import BudgetAgent
from agents.spending_agent import SpendingAgent
from agents.save_agent import SaveAgent
from agents.invest_agent import InvestAgent
from agents.chat_agent import ChatAgent

# Set wide layout
st.set_page_config(page_title="💰 Multi-Agent Finance Assistant", layout="wide")

# --- Custom CSS styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #f4f6f9;
    }

    .main {
        background-color: light Blue;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 0 8px rgba(0, 0, 0, 0.05);
    }

    .block-container {
        padding-top: 20px;
    }

    h1, h2, h3, .stMarkdown {
        font-family: 'Segoe UI', sans-serif;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ---
st.markdown("<h1 style='text-align: center;'>💼 Multi-Agent Finance Assistant</h1>", unsafe_allow_html=True)

# --- Initialize Agents ---
budget_agent = BudgetAgent()
spending_agent = SpendingAgent()
summary = budget_agent.get_summary()

# ---------- 🔼 TOP SECTION ----------
top_left, top_right = st.columns(2)

# --- LEFT: Add Transaction + Summary ---
with top_left:
    st.subheader("➕ Add Transaction")
    with st.form("add_transaction"):
        trans_type = st.selectbox("Type", ["Income", "Expense"])
        category = st.text_input("Category (e.g., Food, Salary)")
        amount = st.number_input("Amount", min_value=0.0, step=1.0)
        submitted = st.form_submit_button("Add")
        if submitted and category and amount > 0:
            budget_agent.add_transaction(trans_type, category, amount)
            st.success("✅ Transaction added successfully!")

    st.subheader("📊 Budget Summary")
    if summary:
        income, expense, balance = summary
        st.metric("Total Income", f"₹ {income:.2f}")
        st.metric("Total Expenses", f"₹ {expense:.2f}")
        st.metric("Current Balance", f"₹ {balance:.2f}")
    else:
        st.warning("No data available.")

# --- RIGHT: Chat Agent ---
with top_right:
    st.subheader("💬 Ask Your Assistant")
    if summary:
        chat_agent = ChatAgent(budget_agent, spending_agent)
        user_query = st.text_input("Ask me anything (e.g., What is my balance?)")
        if user_query:
            response = chat_agent.answer_query(user_query)
            st.info(response)
    else:
        st.warning("Add some transactions first to use the assistant.")

# ---------- ⬇️ MIDDLE SECTION ----------
mid1, mid2 = st.columns([1.5, 1])

# --- LEFT: Expense Table + Top Categories ---
with mid1:
    st.subheader("📂 Expense Category Breakdown")
    category_df = budget_agent.get_category_breakdown()
    if not category_df.empty:
        st.dataframe(category_df)

        st.subheader("🔝 Top Spending Categories")
        top_cats = spending_agent.get_top_categories()
        if not top_cats.empty:
            st.dataframe(top_cats)
        else:
            st.info("No top categories yet.")
    else:
        st.info("No expenses recorded.")

# --- RIGHT: Pie Chart ---
with mid2:
    st.subheader("📈 Expense Pie Chart")
    if not category_df.empty:
        fig, ax = plt.subplots()
        ax.pie(category_df['Amount'], labels=category_df['Category'], autopct='%1.1f%%')
        ax.axis("equal")
        st.pyplot(fig)
    else:
        st.info("Add expense data to see chart.")

# ---------- ⬇️ BOTTOM SECTION ----------
st.divider()
bottom1, bottom2 = st.columns(2)

# --- LEFT: Alerts ---
with bottom1:
    st.subheader("🚨 Overspending Alerts")
    alerts = spending_agent.get_alerts()
    if alerts:
        for cat, spent, limit in alerts:
            st.error(f"⚠️ Overspent in **{cat}** → ₹{spent:.2f} (Limit: ₹{limit})")
    else:
        st.success("✅ All spending is within limits.")

# --- RIGHT: Savings + Investment ---
with bottom2:
    st.subheader("💸 Savings Advice & 💹 Investment Tips")
    if summary:
        save_agent = SaveAgent(income, expense)
        invest_agent = InvestAgent(income, expense)

        saving_advice = save_agent.calculate_saving_advice()
        invest_tips = invest_agent.suggest_investment()

        st.info(saving_advice)
        st.success(invest_tips)
    else:
        st.warning("Please add some income and expenses first.")

# --- DOWNLOAD  CSV REPORT ---
st.divider()
st.subheader("📥 Download Your Full Report")

df = pd.read_csv("data/transactions.csv")

# ✅ Format the 'Date' column nicely
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime("%Y-%m-%d")  # Or use "%d-%m-%Y" if you prefer

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Transactions CSV",
    data=csv,
    file_name="my_transactions_report.csv",
    mime="text/csv"
)
