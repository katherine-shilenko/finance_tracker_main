"""Main dashboard view."""

import tkinter.font
import customtkinter
from controller.controller import Controller
from gui.exit_button import ExitButton


class Dashboard():
    """Main application dashboard with navigation."""

    def __init__(self, root: customtkinter.CTk, controller: Controller, app_title: str) -> None:
        """Initialize dashboard."""
        self.root = root
        self.controller = controller
        self.root.title(app_title)
        self.root.geometry("1350x700")

        # Set the theme, default is dark mode, dark-blue theme color
        self.set_theme()

        # Fill the layout
        self.create_widgets()

    def set_theme(self, mode: str = "dark", theme: str = "dark-blue", fg_color: str = "#0f172a") -> None:
        """Set the main theme of the Dashboard page."""
        customtkinter.set_appearance_mode(mode)
        customtkinter.set_default_color_theme(theme)
        self.root.configure(fg_color=fg_color)

    def create_widgets(self) -> None:
        """Create dashboard widgets."""

        # Configure rows -- control VERTICAL stretching
        # There are 4 main areas
        self.root.grid_rowconfigure(0, weight=3)    # Dashboard title area
        self.root.grid_rowconfigure(1, weight=1)    # Add Transaction button
        self.root.grid_rowconfigure(2, weight=1)    # View All Transactions button
        self.root.grid_rowconfigure(3, weight=5)    # Footer area

        # Configure columns -- control HORIZONTAL stretching
        self.root.grid_columnconfigure(0, weight=1)

        # Dashboard Title
        self.page_title = customtkinter.CTkLabel(self.root,
                                            text="DASHBOARD",
                                            font=("Segoe UI Light", 54),
                                            text_color="#e2e8f0")
        self.page_title.grid(row=0, column=0, pady=(35), sticky="n")        # sticky: forces the label to be stuck in a certain position: s (south), n, etc.

        # Add Transaction button
        self.add_button = customtkinter.CTkButton(self.root,
                                                  text="ADD TRANSACTION",
                                                  font=("Segoe UI", 14),
                                                  width=500,
                                                  height=55,
                                                  fg_color="#6366f1",
                                                  border_width=0.5,
                                                  border_color="#94a3b8",
                                                  hover_color="#818cf8",
                                                  command=self.open_add_transaction
                                                  )
        self.add_button.grid(row=1, column=0, pady=(10))

        # View All Transactions button
        self.view_all_button = customtkinter.CTkButton(self.root,
                                                       command = self.view_all_transactions,
                                                        text="VIEW ALL TRANSACTIONS",
                                                        font=("Segoe UI", 14),
                                                        width=500,
                                                        height=55,
                                                        fg_color="#1e293b",
                                                        border_width=0.5,
                                                        border_color="#94a3b8",
                                                        hover_color="#324461")
        self.view_all_button.grid(row=2, column=0,sticky="n")

        # Footer - mission statement
        self.footer_title = customtkinter.CTkLabel(
            self.root,
            text="Finance, simplified.",
            font=("Segoe UI", 16))
        self.footer_title.grid(row=3, column=0, pady=(15, 0))

        self.footer_subtitle = customtkinter.CTkLabel(
            self.root,
            text="The free desktop tracker that works offline with no account or sign-up needed.",
            font=("Segoe UI", 11),
            text_color="gray"
        )
        self.footer_subtitle.grid(row=3, column=0, pady=(75, 0))

        # Add an exit program option
        self.exit_button = ExitButton.create_button(self.root)
        self.exit_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor="se")

    def open_add_transaction(self) -> None:
        """Open Add Transaction window/form."""
        from gui.add_transaction import AddTransaction
        AddTransaction(self.root, self.controller)

    def view_all_transactions(self) -> None:
        """
        Open 'View All Transactions window/form' as a new window.
        The Dashboard window is automatically closed/destroyed.
        """

        # Clear all widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # After destruction, add a quick delay to avoid overlap in content/layout
        self.root.after(10, self.load_view_all)

    def load_view_all(self) -> None:
        # Create ViewAll to replace the dashboard
        from gui.view_all import ViewAll
        ViewAll(self.root, self.controller)

