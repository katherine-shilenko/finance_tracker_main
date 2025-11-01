"""Add Transaction window view."""

import customtkinter
from controller.controller import Controller

PRIMARY_TEXT_COLOR = "#e2e8f0"
SECONDARY_TEXT_COLOR = "#5d6a7d"
SECONDARY_BG_COLOR = "#0f172a"
PRIMARY_BG_COLOR = "#1e293b"

class AddTransaction:
    """Form window for creating new transactions."""

    def __init__(self, parent: customtkinter.CTk, controller: Controller) -> None:
        """Initialize Add Transaction window/form."""
        self.controller = controller
        self.window = customtkinter.CTkToplevel(parent, fg_color="#1e293b")
        self.window.title("Add Transaction")
        self.window.geometry("500x600")
        self.window.wm_transient(parent)    # ensures that the window pops up on top of the main dashboard window

        # Add widgets to the window
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create form widgets."""

        # Window title (Add Transaction)
        title_label = customtkinter.CTkLabel(self.window,
                                             text="Add Transaction",
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

        self.date_entry = customtkinter.CTkEntry(self.window,
                                                 width=300,
                                                 height=45,
                                                 placeholder_text="YYYY-MM-DD",
                                                 placeholder_text_color=SECONDARY_TEXT_COLOR,
                                                 fg_color=SECONDARY_BG_COLOR,
                                                 border_color=SECONDARY_BG_COLOR)
        self.date_entry.pack(pady=5, padx=40, fill="x")

        # Amount field
        amount_label = customtkinter.CTkLabel(self.window,
                                              font=("Segoe UI", 15),
                                              text="Amount *",
                                              anchor="w")
        amount_label.pack(pady=(10,0), padx=40, fill="x")

        self.amount_entry = customtkinter.CTkEntry(self.window,
                                                   height=45,
                                                   width=300,
                                                   placeholder_text="0.00",
                                                   placeholder_text_color=SECONDARY_TEXT_COLOR,
                                                   fg_color=SECONDARY_BG_COLOR,
                                                   border_color=SECONDARY_BG_COLOR
                                                   )
        self.amount_entry.pack(pady=5, padx=40, fill="x")

        # Category dropdown
        category_label = customtkinter.CTkLabel(self.window,
                                                font=("Segoe UI", 15),
                                                text="Category *",
                                                anchor="w")
        category_label.pack(pady=(10, 0), padx=40, fill="x")

        categories = [
            "Rent", "Food", "Entertainment", "Utilities", "Transportation",
            "Healthcare", "Shopping", "Take-out", "Household Supplies",
            "Travel", "Personal Care", "Miscellaneous"
        ]
        self.category_entry = customtkinter.CTkComboBox(self.window,
                                                        button_color=SECONDARY_BG_COLOR,
                                                        button_hover_color=PRIMARY_BG_COLOR,
                                                        height=45,
                                                        values=categories,
                                                        width=300,
                                                        fg_color=SECONDARY_BG_COLOR,
                                                        border_color=SECONDARY_BG_COLOR,)
        self.category_entry.pack(pady=5, padx=40, fill="x")

        # Notes field
        notes_label = (customtkinter.CTkLabel(self.window,
                                              font=("Segoe UI", 15),
                                              text="Notes (Optional)",
                                              anchor="w"))
        notes_label.pack(pady=(10, 0), padx=40, fill="x")

        self.notes_entry = customtkinter.CTkTextbox(self.window,
                                                    width=300,
                                                    height=100,
                                                    fg_color=SECONDARY_BG_COLOR,
                                                    border_color=SECONDARY_BG_COLOR)
        self.notes_entry.pack(pady=5, padx=40, fill="x")

        # Buttons
        button_frame = customtkinter.CTkFrame(self.window, fg_color="transparent")
        button_frame.pack(pady=(40,20), padx=40, fill="x")

        save_button = (customtkinter.CTkButton(button_frame,
                                               font=("Segoe UI", 15),
                                               text="SAVE",
                                               text_color=PRIMARY_TEXT_COLOR,
                                               fg_color="#10b981",
                                               hover_color="#34d399",
                                               height=40,
                                               width=200,
                                               corner_radius=10))
        save_button.pack(side="left", padx=5)
        cancel_button = (customtkinter.CTkButton(button_frame,
                                                 font=("Segoe UI Light", 15),
                                                 text="CANCEL",
                                                 text_color=PRIMARY_TEXT_COLOR,
                                                 fg_color="#424e61",
                                                 hover_color="#5b6b85",
                                                 height=40,
                                                 width=200,
                                                 corner_radius=10))
        cancel_button.pack(side="left", padx=5)
