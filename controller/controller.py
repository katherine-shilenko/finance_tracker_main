# Author: Ekaterina Shilenko
# Created: October 30th, 2025
# Last Modified: October 30th, 2025
# Description: Controller -- coordinates flow between GUI and DB.

from database.db import DB

class Controller:
    """Controller layer that handles business logic and validation"""

    def __init__(self):
        """Initialize a database"""
        self.db = DB()

    def add_transaction(self, date, amount, category, notes=""):
        """Add a new transaction"""
        # FIXME: ADD INPUT VALIDATION
        self.db.add_transaction(date, amount, category, notes)

    def delete_transaction(self, trans_id):
        """Delete a transaction using unique ID"""
        self.db.delete_transaction(trans_id)

    def update_transaction(self, trans_id, date, amount, category, notes=""):
        """Edit an existing transaction"""
        # FIXME: ADD INPUT VALIDATION
        self.db.update_transaction(trans_id, date, amount, category, notes)

    def get_all_transactions(self):
        """Retrieve all transactions"""
        return self.db.get_all_transactions()

    def close(self):
        """Close DB connection"""
        self.db.close()
