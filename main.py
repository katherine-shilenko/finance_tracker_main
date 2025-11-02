import customtkinter
from database.db import DB
from gui.dashboard import Dashboard

APP_TITLE = "Budget Mini"

if __name__ == "__main__":
    db = DB()
    root = customtkinter.CTk()
    app = Dashboard(root, db, APP_TITLE)
    root.mainloop()
