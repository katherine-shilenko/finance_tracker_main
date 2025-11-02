"""View All Transactions view."""

import customtkinter
from controller.controller import Controller
from CTkTable import CTkTable

PRIMARY_TEXT_COLOR = "#e2e8f0"
SECONDARY_TEXT_COLOR = "#5d6a7d"
SECONDARY_BG_COLOR = "#0f172a"
PRIMARY_BG_COLOR = "#1e293b"


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
        table_headers = ["DATE", "CATEGORY", "AMOUNT", "NOTES", "ACTIONS"]

        if not transactions:
            # If there are no recorded transactions, state so
            table_data = ["You have no transactions"]
        else:
            # If data is present, fill the table
            table_data = [table_headers]

            for expense in transactions:
                # Action icons
                actions = "✏️  🗑️"
                # Collected data
                trans_id, category, amount, date, notes = expense

                table_data.append([date, category, amount, notes, actions])

        # Create a CTkTable
        self.table = CTkTable(self.table_container,
                              row=len(table_data),
                              column=5,
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
                              wraplength=250
                              )
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

    def return_to_dashboard(self):
        pass

    def on_row_click(self):
        pass



