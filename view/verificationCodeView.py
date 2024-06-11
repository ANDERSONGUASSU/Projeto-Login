from customtkinter import CTkToplevel, CTkFrame, CTkLabel, CTkEntry, CTkButton
from controller.controllerUser import UserController
from view.resetPasswordView import ResetPasswordView


class VerificationCodeView(CTkToplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.user_controller = UserController()
        self.email = email
        self.title("Recuperar Senha")

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

        self.code_label = CTkLabel(
            self.frame,
            text="Digite o codigo de verificação",
        )
        self.code_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="e",
        )

        self.code_entry = CTkEntry(self.frame)
        self.code_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )
        self.send_code_button = CTkButton(
            self.frame,
            text="Enviar Código",
            command=self.verify_code,
        )
        self.send_code_button.grid(
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

    def verify_code(self):
        code = self.code_entry.get()
        if self.user_controller.check_verification_code(self.email, code):
            self.destroy()
            ResetPasswordView(self.master, self.email)
