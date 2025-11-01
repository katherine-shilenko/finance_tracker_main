"""
Database handler for transaction storage and retrieval.

This module provides the MODEL layer for the Finance Tracker application.
It handles all direct database interactions using SQLite.
"""

import sqlite3

DATABASE_NAME = "transactions.db"


class DB:
    """Manage SQLite database operations for transactions."""
    def __init__(self, db_name=DATABASE_NAME) -> None:
        """Initialize database connection and create tables if needed."""
        self.connection = None
        self.cursor = None
        try:
            # Create the database connection
            self.connection = sqlite3.connect(DATABASE_NAME)
            # Create cursor object to execute SQL statements
            # and fetch results from SQL queries
            self.cursor = self.connection.cursor()
            print(f"\nSuccessfully connected to {DATABASE_NAME}.")

        except sqlite3.Error as error:
            print(f"Database error occurred: {error}")
        except Exception as error:
            # All other errors
            print(f"An unexpected error occurred: {error}")

        self.create_table()

    def create_table(self) -> None:
        """Create transactions table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                notes TEXT
            )
        """)
        self.connection.commit()

    def add_transaction(self, date: str, amount: float, category: str, notes: str = "") -> None:
        """
        Insert a new transaction.
        """
        self.cursor.execute("""
            INSERT INTO transactions (date, amount, category, notes)
                VALUES (?, ?, ?, ?)
        """, (date, amount, category, notes))
        self.connection.commit()

    def get_all_transactions(self) -> list[tuple]:
        """Retrieve all transactions, sorted by date descending."""

        # SELECT returns a data set, and so we must use fetchall to return data
        self.cursor.execute("""SELECT * FROM transactions ORDER BY date DESC""")
        return self.cursor.fetchall()

    def update_transaction(self, trans_id: int, date: str, amount: float, category: str, notes: str = "") -> None:
        """Update an existing transaction."""
        self.cursor.execute("""UPDATE transactions SET date=?, amount=?, category=?, notes=? WHERE id=?""",
                            (date, amount, category, notes, trans_id))
        self.connection.commit()

    def delete_transaction(self, trans_id: int) -> None:
        """Delete a transaction by ID."""
        self.cursor.execute("""DELETE FROM transactions WHERE id=?""", (trans_id,))
        self.connection.commit()

    def close(self) -> None:
        """Close database connection."""
        self.connection.close()
