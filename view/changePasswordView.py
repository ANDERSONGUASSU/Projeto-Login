import os
from customtkinter import CTkToplevel, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from controller.controllerUser import UserController
from PIL import Image


class ChangePasswordView(CTkToplevel):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.user_controller = UserController()
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

        image_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
            "assets",
            "img",
        )
        self.eye_icon = CTkImage(Image.open(os.path.join(image_path, "Eye.png")))
        self.closed_eye_icon = CTkImage(
            Image.open(os.path.join(image_path, "Closed_Eye.png"))
        )

        self.password_label = CTkLabel(
            self.frame,
            text="Atualize sua senha",
        )
        self.password_label.grid(
            row=0,
            columnspan=2,
            pady=5,
            padx=5,
        )

        self.old_password_label = CTkLabel(
            self.frame,
            text="Senha:",
        )
        self.old_password_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.old_password_entry = CTkEntry(
            self.frame,
            show="*",
        )
        self.old_password_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )

        self.show_old_password = False
        self.old_toggle_button = CTkButton(
            self.frame,
            text="",
            image=self.closed_eye_icon,
            width=3,
            command=self.toggle_old_password,
        )
        self.old_toggle_button.grid(
            row=1,
            column=2,
        )

        self.new_password_label = CTkLabel(
            self.frame,
            text="Nova senha:",
        )
        self.new_password_label.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="we",
        )

        self.new_password_entry = CTkEntry(
            self.frame,
            show="*",
        )
        self.new_password_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w",
        )

        self.show_new_password = False
        self.new_toggle_button = CTkButton(
            self.frame,
            text="",
            image=self.closed_eye_icon,
            width=3,
            command=self.toggle_new_password,
        )
        self.new_toggle_button.grid(
            row=2,
            column=2,
        )

        self.update_password_button = CTkButton(
            self.frame,
            text="Atualizar Senha",
            command=self.update_password,
        )
        self.update_password_button.grid(
            row=3,
            column=0,
            pady=10,
        )

        self.back_button = CTkButton(
            self.frame,
            text="Voltar",
            command=self.destroy,
        )
        self.back_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=10,
        )

    def toggle_old_password(self):
        if self.show_old_password:
            self.old_password_entry.configure(show="*")
            self.old_toggle_button.configure(image=self.closed_eye_icon)
        else:
            self.old_password_entry.configure(show="")
            self.old_toggle_button.configure(image=self.eye_icon)
        self.show_old_password = not self.show_old_password

    def toggle_new_password(self):
        if self.show_new_password:
            self.new_password_entry.configure(show="*")
            self.new_toggle_button.configure(image=self.closed_eye_icon)
        else:
            self.new_password_entry.configure(show="")
            self.new_toggle_button.configure(image=self.eye_icon)
        self.show_new_password = not self.show_new_password

    def update_password(self):
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()

        if hasattr(self, 'message_label'):
            self.message_label.destroy
        if hasattr(self, 'error_label'):
            self.error_label.destroy

        if self.user.check_password(old_password):
            success, message = self.user_controller.update_password(
                self.user.email,
                new_password,
            )
            if success is True:

                self.message_label = CTkLabel(
                    self.frame,
                    text=message,
                )
                self.message_label.grid(
                    row=4,
                    columnspan=2,
                )
                self.after(2000, self.destroy)
            else:
                self.message_label = CTkLabel(
                    self.frame,
                    text=message,
                )
                self.message_label.grid(
                    row=4,
                    columnspan=2,
                )
        else:
            self.error_label = CTkLabel(
                self.frame,
                text='Senha antiga incorreta',
            )
            self.error_label.grid(
                row=4,
                columnspan=2,
            )
