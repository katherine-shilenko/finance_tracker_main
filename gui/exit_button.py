import customtkinter


class ExitButton:
    """A reusable button to exit the main application window."""
    def create_button(parent: customtkinter.CTk) -> customtkinter.CTkButton:
        def exit_application():
            """Destroy the main root window, fully exiting the program."""
            parent.winfo_toplevel().destroy()

        # Create and configure the actual button widget
        exit_button = customtkinter.CTkButton(
            parent,
            text="EXIT PROGRAM",
            command=exit_application,
            font=("Segoe UI", 12),
            width=150,
            height=50,
            fg_color="#f55858",
            hover_color="#f77979")

        return exit_button
