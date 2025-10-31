import tkinter.font
import customtkinter

class Dashboard():
    def __init__(self, root, db, app_title):
        # Initialize the main window
        self.root = root
        self.db = db
        self.root.title(app_title)
        self.root.geometry("1350x700")

        # Set the theme, default is dark mode, dark-blue theme color
        self.set_theme()

        # Fill the layout
        self.fill_main()

    def set_theme(self, mode="dark", theme="dark-blue", fg_color="#0f172a"):
        """"Set the main theme of the Dashboard page"""
        customtkinter.set_appearance_mode(mode)
        customtkinter.set_default_color_theme(theme)
        self.root.configure(fg_color=fg_color)

    def fill_main(self):
        """Fill the root window"""
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
                                                  font=("Segoe UI Light", 14),
                                                  width=500,
                                                  height=60,
                                                  fg_color="#818cf8",
                                                  border_width=2
                                                  )
        self.add_button.grid(row=1, column=0, pady=(10))

        # View All Transactions button
        self.view_all_button = customtkinter.CTkButton(self.root,
                                                  text="VIEW ALL TRANSACTION",
                                                  font=("Segoe UI Light", 14),
                                                  width=500,
                                                  height=60,
                                                  fg_color="#1e293b",
                                                  border_width=2
                                                  )
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

        # USE TO CHECK ALL AVAILABLE FONTS
        # available_fonts = sorted(tkinter.font.families())
        # for font_family in available_fonts:
            # print(font_family)

