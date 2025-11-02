"""View All Transactions view."""

import customtkinter
from controller.controller import Controller
from CTkTable import CTkTable

PRIMARY_TEXT_COLOR = "#e2e8f0"
SECONDARY_TEXT_COLOR = "#5d6a7d"
SECONDARY_BG_COLOR = "#0f172a"
PRIMARY_BG_COLOR = "#1e293b"
APP_TITLE = "Budget Mini"


class ViewAll():
    """Table view for displaying all transactions."""

    def __init__(self, parent: customtkinter.CTk, controller: Controller) -> None:
        """Initialize View All Transactions window with styling."""
        self.root = parent
        self.controller = controller

        # Update page properties
        self.root.title("View All Transactions")
        self.root.geometry("1350x700")

        # Fill the page
        self.create_widgets()
        self.populate_table()

    def create_widgets(self) -> None:
        """Create and layout table and buttons."""

        # Top frame with table title and Add button
        top_frame = customtkinter.CTkFrame(self.root, fg_color="transparent")
        top_frame.pack(padx=250, pady=(120, 30), fill="x")

        # Table title label
        table_title_label = customtkinter.CTkLabel(
            top_frame,
            text="All Transactions",
            font=("Segoe UI Light", 30),
            text_color="#e2e8f0")
        table_title_label.pack(side="left")

        # Add Transaction button
        add_transaction_button = customtkinter.CTkButton(
            top_frame,
            text="ADD TRANSACTION",
            command=self.open_add_window,
            font=("Segoe UI", 14),
            width=250,
            height=55,
            fg_color="#6366f1",
            border_width=0.5,
            border_color="#94a3b8",
            hover_color="#818cf8")
        add_transaction_button.pack(side="right")

        # Table container frame
        self.table_container = customtkinter.CTkScrollableFrame(self.root,
                                                                fg_color="transparent", corner_radius=12)
        self.table_container.pack(padx=250, pady=(0, 20), fill="both", expand=True)

        # Bottom button (Return to Dashboard)
        back_to_dash = customtkinter.CTkButton(self.root,
                                               text="RETURN TO DASHBOARD",
                                               command=self.return_to_dashboard,
                                               fg_color="#1e293b",
                                               hover_color="#324461",
                                               font=("Segoe UI", 15),
                                               height=50,
                                               corner_radius=10,
                                               text_color=PRIMARY_TEXT_COLOR
                                               )
        back_to_dash.pack(padx=250, pady=(30, 120), fill="x")

    def populate_table(self):
        """Populate table contents."""

        # Get all transactions
        transactions = self.controller.get_all_transactions()

        # Prepare table data
        table_headers = ["DATE", "CATEGORY", "AMOUNT", "NOTES", "EDIT", "DELETE"]

        if not transactions:
            # If there are no recorded transactions, state so
            no_transactions_label = customtkinter.CTkLabel(self.table_container,
                                                           text="You have no recorded transactions.",
                                                           text_color=PRIMARY_TEXT_COLOR,
                                                           font=("Segoe UI", 15))
            no_transactions_label.pack(pady=20)
        else:
            # If data is present, fill the table
            table_data = [table_headers]

            # Store transaction IDs for reference
            self.transaction_ids = []

            for expense in transactions:
                # Collected data
                trans_id, category, amount, date, notes = expense

                # Store transaction ID
                self.transaction_ids.append(trans_id)

                table_data.append([date, category, amount, notes, "✏️", "🗑️"])

            # Create a CTkTable
            self.table = CTkTable(self.table_container,
                              row=len(table_data),
                              column=6,
                              values=table_data,
                              colors=["#1e293b", "#324461"],
                              header_color="#0c1221",
                              hover_color="#818cf8",
                              text_color=PRIMARY_TEXT_COLOR,
                              font=("Segoe UI Light", 15),
                              corner_radius=10,
                              padx=1,
                              pady=1,
                              command=self.on_row_click,
                              height=40,
                              wraplength=250)
            self.table.pack(fill="both", expand=True)


    def open_add_window(self):
        """Open Add Transaction window/form."""
        from gui.add_transaction import AddTransaction
        add_window = AddTransaction(self.root, self.controller)

        # Wait for the window to close before refreshing
        self.root.wait_window(add_window.window)

        # Destroy existing table if it exists to avoid data overlap after performing actions
        if self.table:
            self.table.destroy()
            self.table = None

        # Refresh the table after window closes
        self.populate_table()

    def on_row_click(self, cell):
        """Handle table cell clicks."""
        row = cell["row"]
        print(f"ROW: {row}")
        col = cell["column"]
        print(f"Column: {col}")

        self.selected_row = row - 1     # -1 accounts for the header row

        if row == 0:  # Ignore header row
            return
        if col == 4:
            self.edit_selected()
        elif col == 5:
            self.delete_selected()


    def delete_selected(self):
        """Delete selected transaction."""
        trans_id = self.transaction_ids[self.selected_row]
        print(trans_id)

        # Create confirmation dialog window
        confirm_window = customtkinter.CTkToplevel(self.root)
        confirm_window.title("Delete")
        confirm_window.geometry("450x250")
        confirm_window.configure(fg_color="#1e293b")

        # Center the dialog
        confirm_window.transient(self.root)     # sets root as the parent, so that the pop-up window stays on top
        confirm_window.grab_set()               # ensures we can't interact with the parent before making a selection on the pop-up

        # Window title
        delete_label = customtkinter.CTkLabel(
            confirm_window,
            text="Delete Transaction?",
            font=("Segoe UI", 28),
            text_color=PRIMARY_TEXT_COLOR)
        delete_label.pack(pady=(20, 20), fill="x")

        # Delete message
        delete_message = customtkinter.CTkLabel(
            confirm_window,
            text="Are you sure you want to delete this \ntransaction? This action cannot be undone.",
            font=("Segoe UI", 14),
            text_color=SECONDARY_TEXT_COLOR)
        delete_message.pack(pady=(0, 40), fill="x")

        def do_delete():
            """Delete the transaction if the user chooses 'Yes, Delete'."""
            self.controller.delete_transaction(trans_id)
            confirm_window.destroy()
            self.selected_row = None

            # Destroy old table and refresh
            if self.table:
                self.table.destroy()
            self.populate_table()

        # Buttons frame
        button_frame = customtkinter.CTkFrame(confirm_window, fg_color="transparent")
        button_frame.pack(pady=(0, 20))

        yes_button = customtkinter.CTkButton(
            button_frame,
            text="YES, DELETE",
            command=do_delete,
            fg_color="#f55858",
            hover_color="#f77979",
            width=200,
            height=50,
            corner_radius=10,
            font=("Segoe UI", 15, "bold")
        )
        yes_button.pack(side="left", padx=10)

        cancel_button = customtkinter.CTkButton(
            button_frame,
            text="NO, CANCEL",
            command=confirm_window.destroy,
            fg_color="#424e61",
            hover_color="#5b6b85",
            width=200,
            height=50,
            corner_radius=10,
            font=("Segoe UI", 15, "bold")
        )
        cancel_button.pack(side="left", padx=10)

    def edit_selected(self):
        pass

    def return_to_dashboard(self):
        """Return to the main dashboard window."""
        from gui.dashboard import Dashboard

        # Clear all widgets from root
        for widget in self.root.winfo_children():
            widget.destroy()

        # Recreate dashboard in the same root window
        Dashboard(self.root, self.controller, APP_TITLE)
