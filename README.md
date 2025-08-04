# 💼 Multi-Agent Finance Assistant

A smart, interactive **finance management app** built with **Streamlit**, using **multiple intelligent agents** to help users manage money, track expenses, visualize financial data, and chat with a financial assistant.

---

## 🚀 Features

- 💬 **Chat Agent**: Ask budget-related questions and get AI replies.
- 💸 **Transaction Agent**: Add income and expense entries with categories.
- 📊 **Summary Agent**: View your current balance, total income, and total expenses.
- 🧾 **Category Breakdown Agent**: See breakdown of expenses per category.
- 🥧 **Visualization Agent**: Get a pie chart showing expense categories.
- 📥 **Download Report**: Export your transactions as a `.csv` file.

---

## 🧠 Tech Stack

| Component          | Tech Used       |
|-------------------|-----------------|
| Framework         | Streamlit       |
| Language          | Python          |
| Data Handling     | Pandas          |
| Styling           | Custom CSS via Streamlit |
| Version Control   | Git + GitHub    |

---

## 🔁 Flowchart

```mermaid
flowchart TD
    A[User Input] --> B[Transaction Agent]
    A --> C[Chat Agent]
    B --> D[Summary Agent]
    B --> E[Category Breakdown Agent]
    B --> F[Pie Chart Agent]
    D --> G[Download CSV
```
🗂️ Project Structure
markdown
Copy
Edit
multi-agent-finance-assistant/
│
├── app.py
├── transactions.csv
├── .gitignore
├── requirements.txt
├── README.md
└── assets/

⚙️ How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/multi-agent-finance-assistant.git
cd multi-agent-finance-assistant
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Start the app

bash
Copy
Edit
streamlit run app.py
Open http://localhost:8501 in your browser.

📦 Requirements
requirements.txt

nginx
Copy
Edit
streamlit
pandas
📁 .gitignore
.gitignore

gitignore
Copy
Edit
__pycache__/
*.pyc
.env
*.csv
📄 License
This project is licensed under the MIT License.


