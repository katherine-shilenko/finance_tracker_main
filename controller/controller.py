"""
Transaction business logic and validation.

This module provides the CONTROL layer for the Finance Tracker application.
"""

from database.db import DB


class Controller:
    """Handle transaction validation and business logic."""

    def __init__(self) -> None:
        """Initialize controller with database handler."""
        self.db = DB()

    def add_transaction(self, date: str, amount: float, category: str, notes: str = "") -> None:
        """Add a new transaction with validation."""

        # FIXME: ADD INPUT VALIDATION
        self.db.add_transaction(date, amount, category, notes)

    def delete_transaction(self, trans_id):
        """Delete a transaction."""
        self.db.delete_transaction(trans_id)

    def update_transaction(self, trans_id: int, date: str, amount: float, category: str, notes: str = "") -> None:
        """Update an existing transaction with validation."""

        # FIXME: ADD INPUT VALIDATION
        self.db.update_transaction(trans_id, date, amount, category, notes)

    def get_all_transactions(self) -> list[tuple]:
        """Retrieve all transactions."""
        return self.db.get_all_transactions()

    def close(self) -> None:
        """Close DB connection."""
        self.db.close()
