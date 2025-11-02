"""Edit Transaction window view."""

import customtkinter
from controller.controller import Controller
from datetime import datetime


PRIMARY_TEXT_COLOR = "#e2e8f0"
SECONDARY_TEXT_COLOR = "#5d6a7d"
SECONDARY_BG_COLOR = "#0f172a"
PRIMARY_BG_COLOR = "#1e293b"

class EditTransaction:
    """Form window for editing an existing transactions."""

    def __init__(self, parent: customtkinter.CTk, controller: Controller, trans_data: tuple) -> None:
        """Initialize Edit Transaction window/form."""
        self.controller = controller
        self.trans_id = trans_data[0]
        self.window = customtkinter.CTkToplevel(parent, fg_color="#1e293b")
        self.window.title("Edit Transaction")
        self.window.geometry("500x600")
        self.window.transient(parent)    # ensures that the window pops up on top of the main dashboard window

        # Add widgets to the window
        self.create_widgets(trans_data)

    def create_widgets(self, trans_data: tuple) -> None:
        """Create form widgets."""

        # Window title (Edit Transaction)
        title_label = customtkinter.CTkLabel(self.window,
                                             text="Edit Transaction",
                                             font=("Segoe UI", 25),
                                             anchor="w",
                                             text_color=PRIMARY_TEXT_COLOR)
        title_label.pack(pady=10, padx=40, fill="x")

        # Date field
        date_label = customtkinter.CTkLabel(self.window,
                                            font=("Segoe UI", 15),
                                            text="Date *",
                                            anchor="w")
        date_label.pack(pady=(10,0), padx=40, fill="x")

        # Locate date in the trans_data
        date_str = trans_data[1]
        self.date_entry = customtkinter.CTkEntry(self.window,
                                                 text_color=PRIMARY_TEXT_COLOR,
                                                 font=("Segoe UI", 15),
                                                 width=300,
                                                 height=45,
                                                 fg_color=SECONDARY_BG_COLOR,
                                                 border_color=SECONDARY_BG_COLOR)
        self.date_entry.insert(0, date_str)
        self.date_entry.pack(pady=5, padx=40, fill="x")

        # Amount field
        amount_label = customtkinter.CTkLabel(self.window,
                                              font=("Segoe UI", 15),
                                              text="Amount *",
                                              anchor="w")
        amount_label.pack(pady=(10,0), padx=40, fill="x")

        # Locate amount in trans_data
        amount_float = trans_data[2]
        self.amount_entry = customtkinter.CTkEntry(self.window,
                                                   text_color=PRIMARY_TEXT_COLOR,
                                                   font=("Segoe UI", 15),
                                                   height=45,
                                                   width=300,
                                                   fg_color=SECONDARY_BG_COLOR,
                                                   border_color=SECONDARY_BG_COLOR
                                                   )
        self.amount_entry.insert(0, str(amount_float))
        self.amount_entry.pack(pady=5, padx=40, fill="x")

        # Category dropdown
        category_label = customtkinter.CTkLabel(self.window,
                                                font=("Segoe UI", 15),
                                                text="Category *",
                                                anchor="w")
        category_label.pack(pady=(10, 0), padx=40, fill="x")

        # Locate category in trans_data
        category_str = trans_data[3]
        categories = [
            "Rent", "Food", "Entertainment", "Utilities", "Transportation",
            "Healthcare", "Shopping", "Take-out", "Household Supplies",
            "Travel", "Personal Care", "Miscellaneous"
        ]
        self.category_entry = customtkinter.CTkComboBox(self.window,
                                                        text_color=PRIMARY_TEXT_COLOR,
                                                        font=("Segoe UI", 15),
                                                        dropdown_font=("Segoe UI", 15),
                                                        button_color=SECONDARY_BG_COLOR,
                                                        button_hover_color="#424e61",
                                                        height=45,
                                                        values=categories,
                                                        width=300,
                                                        dropdown_hover_color="#424e61",
                                                        fg_color=SECONDARY_BG_COLOR,
                                                        dropdown_fg_color=SECONDARY_BG_COLOR,
                                                        border_color=SECONDARY_BG_COLOR,
                                                        )
        self.category_entry.set(category_str)
        self.category_entry.pack(pady=5, padx=40, fill="x")

        # Notes field
        notes_label = (customtkinter.CTkLabel(self.window,
                                              font=("Segoe UI", 15),
                                              text="Notes (Optional)",
                                              anchor="w"))
        notes_label.pack(pady=(10, 0), padx=40, fill="x")

        # Locate notes in trans_data
        notes_str = trans_data[4]
        self.notes_entry = customtkinter.CTkTextbox(self.window,
                                                    text_color=PRIMARY_TEXT_COLOR,
                                                    width=300,
                                                    height=100,
                                                    fg_color=SECONDARY_BG_COLOR,
                                                    border_color=SECONDARY_BG_COLOR)
        self.notes_entry.insert("1.0", notes_str)
        self.notes_entry.pack(pady=5, padx=40, fill="x")

        # Buttons
        button_frame = customtkinter.CTkFrame(self.window, fg_color="transparent")
        button_frame.pack(pady=(40,20), padx=40, fill="x")

        save_button = (customtkinter.CTkButton(button_frame,
                                               command=self.save,
                                               font=("Segoe UI", 15),
                                               text="SAVE CHANGES",
                                               text_color=PRIMARY_TEXT_COLOR,
                                               fg_color="#10b981",
                                               hover_color="#34d399",
                                               height=40,
                                               width=200,
                                               corner_radius=10))
        save_button.pack(side="left", padx=5)

        cancel_button = (customtkinter.CTkButton(button_frame,
                                                 command=self.window.destroy,
                                                 font=("Segoe UI", 15),
                                                 text="CANCEL",
                                                 text_color=PRIMARY_TEXT_COLOR,
                                                 fg_color="#424e61",
                                                 hover_color="#5b6b85",
                                                 height=40,
                                                 width=200,
                                                 corner_radius=10))
        cancel_button.pack(side="left", padx=5)

    def save(self) -> None:
        """Update transaction via controller."""

        # Collect new/old data from all input fields
        date = self.date_entry.get().strip()
        amount = self.amount_entry.get().strip()
        category = self.category_entry.get().strip()
        notes = self.notes_entry.get("1.0", "end-1c").strip()

        # We need transaction id to update -- how do I find that

        # Add Transaction
        self.controller.update_transaction(self.trans_id, date, amount, category, notes)

        # Destroy the window
        self.window.after(1000, self.window.destroy)
