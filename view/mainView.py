from customtkinter import CTkLabel, CTkButton, CTk
from view.changePasswordView import ChangePasswordView


class MainView(CTk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title("Tela Principal")

        width = 900
        height = 500

        win_width = self.winfo_screenwidth()
        win_height = self.winfo_screenheight()

        x = (win_width - width) // 1.5
        y = (win_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.welcome_label = CTkLabel(
            self,
            text="Bem vindo",
        )
        self.welcome_label.pack()

        self.exit_button = CTkButton(
            self,
            text="Sair",
            command=self.exit,
        )
        self.exit_button.pack(pady=10)

        self.logout_button = CTkButton(
            self,
            text="Logout",
            command=self.logout,
        )
        self.logout_button.pack(pady=10)

        self.change_password_button = CTkButton(
            self,
            text="Trocar Senha",
            command=self.change_password,
        )
        self.change_password_button.pack(pady=10)

    def exit(self):
        self.destroy()

    def logout(self):
        self.destroy()
        from view.logingView import LoginView

        LoginView()

    def change_password(self):
        ChangePasswordView(self, self.user)
