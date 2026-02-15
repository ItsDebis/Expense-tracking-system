# Expense Tracking System

A Python-based Expense Tracking System to manage daily expenses, categorize transactions, and analyze spending patterns. Built using **FastAPI**, **Streamlit**, and **MySQL** with full CRUD functionality and a monthly analytics dashboard.

---

## Application Demo

![Application Demo](assets/demo.gif)

---

## Screenshots

### Add / Update Expenses
![Add and Update](assets/Add_and_Update.png)

### Analytics By Category
![Analytics By Category](assets/Analytics_by_Category.png)

### Analytics By Months
![Analytics By Months](assets/Analytics_by_Monthly.png)

---

## Features

- Add, update, and delete daily expenses  
- Categorize transactions (Food, Shopping, Entertainment, Rent, etc.)  
- Date-based expense tracking  
- Category-wise analytics with percentage breakdown  
- Monthly expense summary by year  
- Interactive dashboard using Streamlit  
- RESTful APIs built with FastAPI  
- MySQL database integration  
- Structured logging  
- Backend and frontend test cases  

---

## Project Structure

```
Expense-tracking-system/
│
├── assets/                 # Demo GIF and screenshots
├── backend/                # FastAPI backend server
│   ├── server.py
│   ├── db_helper.py
│   └── logging_setup.py
│
├── frontend/               # Streamlit frontend UI
│   ├── app.py
│   ├── add_update_ui.py
│   ├── analytics_by_category.py
│   └── monthly_analytics_ui.py
│
├── tests/                  # Unit tests
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/ItsDebis/Expense-tracking-system.git
cd Expense-tracking-system
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Configure MySQL

- Create a database named `expense_manager`
- Create the required `expenses` table
- Update credentials inside `backend/db_helper.py` if needed

### 4. Run the FastAPI backend

```
uvicorn backend.server:app --reload
```

Backend runs at:  
http://127.0.0.1:8000

### 5. Run the Streamlit frontend

```
streamlit run frontend/app.py
```

Frontend runs at:  
http://localhost:8501

---

## Tech Stack

- Python 3.10  
- FastAPI  
- Streamlit  
- MySQL  
- Uvicorn  
- Pytest  

---

## Future Improvements

- User authentication  
- Export reports (CSV / PDF)  
- Cloud deployment  
- Docker containerization  

---

## Author

Built as a full-stack backend and frontend integration project demonstrating API development, database management, and dashboard analytics.
