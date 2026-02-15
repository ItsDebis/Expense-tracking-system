import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)

    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT amount, category, notes FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
        return cursor.fetchall()


def delete_expenses_for_date(expense_date):
    logger.info(f"Deleting expenses for {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting expense: {expense_date}, {amount}, {category}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO expenses (expense_date, amount, category, notes)
            VALUES (%s, %s, %s, %s)
            """,
            (expense_date, amount, category, notes)
        )


def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )
        return cursor.fetchall()


def fetch_monthly_summary_by_year(year):
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT
                MONTH(expense_date) AS month,
                MONTHNAME(expense_date) AS month_name,
                SUM(amount) AS total
            FROM expenses
            WHERE YEAR(expense_date) = %s
            GROUP BY month, month_name
            ORDER BY month
            """,
            (year,)
        )
        return cursor.fetchall()
