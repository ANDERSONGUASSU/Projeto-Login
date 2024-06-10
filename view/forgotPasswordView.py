import random
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from customtkinter import CTkToplevel, CTkFrame, CTkLabel, CTkEntry, CTkButton
from controller.controllerUser import UserController
from view.verificationCodeView import VerificationCodeView

load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


class ForgotPasswordView(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.user_controller = UserController()
        self.title("Recuperar senha")

        width = 900
        height = 500

        win_width = self.winfo_screenwidth()
        win_height = self.winfo_screenheight()

        x = (win_width - width) // 1.5
        y = (win_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.frame = CTkFrame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.email_label = CTkLabel(self.frame, text="Digite seu email")
        self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.email_entry = CTkEntry(self.frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.send_code_button = CTkButton(
            self.frame, text="Enviar Código", command=self.send_verification_code
        )
        self.send_code_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=10,
        )

        self.back_button = CTkButton(self.frame, text="Voltar", command=self.destroy)
        self.back_button.grid(
            row=1,
            column=1,
            padx=5,
            pady=10,
        )

    def send_verification_code(self):
        email = self.email_entry.get()
        user = self.user_controller.get_user_by_email(email)
        if user:
            verification_code = "".join([str(random.randint(0, 9)) for _ in range(6)])
            self.user_controller.save_verification_code(email, verification_code)
            self.send_email(email, verification_code)
            self.destroy()
            VerificationCodeView(self.master, email)
        else:
            self.erro_label = CTkLabel(self.frame, text="Email não encontrado")
            self.erro_label.grid(row=2, columnspan=2, padx=5, pady=5, sticky="ew")

    def send_email(self, email, code):
        msg = MIMEText(f"Seu código de verificação é {code}")
        msg["Subject"] = "Código de Verificação"
        msg["From"] = f"{EMAIL}"
        msg["To"] = email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(f"{EMAIL}", f"{EMAIL_PASSWORD}")
                server.sendmail(f"{EMAIL}", email, msg.as_string())
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
