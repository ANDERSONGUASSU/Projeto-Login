from customtkinter import CTkToplevel, CTkFrame, CTkLabel, CTkEntry, CTkButton
from controller.controllerUser import UserController


class RegisterView(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.user_controller = UserController()
        self.title("Cadastrar novo usuário")

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

        self.name_label = CTkLabel(
            self.frame,
            text="Nome completo:",
        )
        self.name_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.name_entry = CTkEntry(self.frame)
        self.name_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )

        self.email_label = CTkLabel(
            self.frame,
            text="E-mail:",
        )
        self.email_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.email_entry = CTkEntry(self.frame)
        self.email_entry.grid(
            row=1,
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
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.password_entry = CTkEntry(self.frame)
        self.password_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )

        self.register_button = CTkButton(
            self.frame,
            text="Cadastrar",
            command=self.register,
        )
        self.register_button.grid(
            row=3,
            column=0,
            pady=10,
            padx=5,
        )

        self.back_button = CTkButton(
            self.frame,
            text="Voltar",
            command=self.back,
        )
        self.back_button.grid(
            row=3,
            column=1,
            pady=10,
            padx=5,
        )

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        (sucess, message) = self.user_controller.create_user(
            nome=name,
            email=email,
            password=password,
        )
        self.message_label = CTkLabel(
            self.frame,
            text=message,
        )
        self.message_label.grid(
            row=3,
            columnspan=2,
            pady=10,
            padx=5,
        )

        if sucess:
            self.destroy()

    def back(self):
        self.destroy()
