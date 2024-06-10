from customtkinter import CTkToplevel, CTkFrame, CTkLabel, CTkEntry, CTkButton
from controller.controllerUser import UserController


class ResetPasswordView(CTkToplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.user_controller = UserController()
        self.email = email
        self.title("Recuperar Senha")

        width = 600
        height = 400

        win_width = self.winfo_screenwidth()
        win_height = self.winfo_screenheight()

        x = (win_width - width) // 2
        y = (win_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.frame = CTkFrame(self)
        self.frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

        self.new_password_label = CTkLabel(
            self.frame,
            text="Digite a nova senha",
        )
        self.new_password_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="e",
        )

        self.new_password_entry = CTkEntry(self.frame)
        self.new_password_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )
        self.update_password_button = CTkButton(
            self.frame,
            text="Atualizar Senha",
            command=self.update_password,
        )
        self.update_password_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=10,
        )

        self.back_button = CTkButton(
            self.frame,
            text="Voltar",
            command=self.destroy,
        )
        self.back_button.grid(
            row=1,
            column=1,
            padx=5,
            pady=10,
        )

    def update_password(self):
        new_password = self.new_password_entry.get()
        (success, message) = self.user_controller.update_password(
            self.email,
            new_password,
        )

        if success:
            self.mensagem_label = CTkLabel(
                self.frame,
                text=f"{message}",
            )
            self.mensagem_label.grid(
                row=2,
                columnspan=2,
                padx=5,
                pady=5,
                sticky="ew",
            )
