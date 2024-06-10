import customtkinter as ctk
from view.logingView import (
    LoginView,
)


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("assets/themes/green.json")

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
