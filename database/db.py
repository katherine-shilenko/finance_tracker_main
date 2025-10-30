# Author: Ekaterina Shilenko
# Created: October 25th, 2025
# Last Modified: October 30th, 2025
# Description: Database handler for the finance tracker app. Handles DB operations: table creation,
#       table item addition, table item deletion, view all table items. Data is stored locally on the client machine.

import sqlite3

DATABASE_NAME = "transactions.db"

class DB:
    def __init__(self, db_name=DATABASE_NAME):
        """Creates the database connection and cursor"""
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

    def create_table(self):
        # SQL query to create a table
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

    def add_transaction(self, date, amount, category, notes):
        # Add a transaction
        self.cursor.execute("""
            INSERT INTO transactions (date, amount, category, notes)
                VALUE (?, ?, ?, ?)
        """, (date, amount, category, notes))
        self.connection.commit()

    def get_all_transactions(self):
        # Returns all transactions
        # SELECT returns a data set, and so we must use fetchall to return data
        self.cursor.execute("""SELECT * FROM transactions ORDER BY date DESC""")
        self.cursor.fetchall()

    def update_transaction(self, trans_id, date, amount, category, notes):
        # Update the transaction
        self.cursor.execute("""UPDATE transactions SET date=?, amount=?, category=?, notes=? WHERE id=?""",
                            (date, amount, category, notes, trans_id))
        self.connection.commit()

    def delete_transaction(self, trans_id):
        # Delete the transaction using its unique id
        self.cursor.execute("""DELETE FROM transactions WHERE id=?""", (trans_id))
        self.connection.commit()

    def close(self):
        # Close the DB/connection
        self.connection.close()
