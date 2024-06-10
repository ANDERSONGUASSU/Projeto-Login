import os
from customtkinter import CTkLabel, CTkEntry, CTkFrame, CTkButton, CTk, CTkImage
from controller.controllerUser import UserController
from view.mainView import MainView
from view.registerView import RegisterView
from view.forgotPasswordView import ForgotPasswordView
from PIL import Image


class LoginView(CTk):
    def __init__(self):
        super().__init__()
        self.user_controller = UserController()
        self.title("Login")

        width = 900
        height = 500

        win_width = self.winfo_screenwidth()
        win_height = self.winfo_screenheight()

        x = (win_width - width) // 1.5
        y = (win_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.frame = CTkFrame(self)
        self.frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

        self.email_label = CTkLabel(
            self.frame,
            text="Email:",
        )
        self.email_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.email_entry = CTkEntry(self.frame)
        self.email_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )

        self.password_label = CTkLabel(
            self.frame,
            text="Senha:",
        )
        self.password_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.password_entry = CTkEntry(
            self.frame,
            show=("*"),
        )
        self.password_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )

        image_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
            "assets",
            "img",
        )
        self.eye_icon = CTkImage(Image.open(os.path.join(image_path, "Eye.png")))
        self.closed_eye_icon = CTkImage(
            Image.open(os.path.join(image_path, "Closed_Eye.png"))
        )

        self.show_password = False
        self.toggle_button = CTkButton(
            self.frame,
            text="",
            image=self.closed_eye_icon,
            width=3,
            command=self.toggle_password,
        )
        self.toggle_button.grid(
            row=1,
            column=2,
        )

        self.login_button = CTkButton(
            self.frame,
            text="Login",
            command=self.login,
        )
        self.login_button.grid(
            row=2,
            column=0,
            pady=10,
            padx=5,
        )

        self.register_button = CTkButton(
            self.frame,
            text="Cadastrar",
            command=self.register_view,
        )
        self.register_button.grid(
            row=2,
            column=1,
            pady=10,
            padx=5,
        )

        self.forgot_password_button = CTkButton(
            self.frame,
            text="Esqueci a senha",
            command=self.forgot_password_view,
        )
        self.forgot_password_button.grid(
            row=3,
            columnspan=2,
            pady=10,
            padx=5,
        )

    def toggle_password(self):
        if self.show_password:
            self.password_entry.configure(show="*")
            self.toggle_button.configure(image=self.closed_eye_icon)
        else:
            self.password_entry.configure(show="")
            self.toggle_button.configure(image=self.eye_icon)
        self.show_password = not self.show_password

    def login(self):
        email = self.email_entry.get()
        senha = self.password_entry.get()
        user = self.user_controller.authenticate_user(email, senha)
        if user:
            self.destroy()
            MainView(user)
        else:
            self.error_label = CTkLabel(
                self.frame,
                text="E-mail ou senha incorretos",
            )
            self.error_label.grid(
                row=4,
                columnspan=2,
                pady=5,
            )

    def register_view(self):
        RegisterView(self)

    def forgot_password_view(self):
        ForgotPasswordView(self)
