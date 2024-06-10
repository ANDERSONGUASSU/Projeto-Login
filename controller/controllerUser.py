from models.models import User, session
from sqlalchemy.exc import IntegrityError


class UserController:
    def get_user_by_email(self, email):
        return session.query(User).filter_by(email=email).first()

    def create_user(self, nome, email, password):
        new_user = User(
            nome=nome,
            email=email,
            password=password,
        )
        try:
            new_user.set_password(password)
            session.add(new_user)
            session.commit()
            return (True, "Usuário criado com sucesso!")
        except IntegrityError:
            session.rollback()
            return (False, "Erro: Email já está em uso.")
        except ValueError as ve:
            return (False, f"Erro: {ve}")

    def authenticate_user(self, email, password):
        user = self.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None

    def update_password(self, email, new_password):
        user = self.get_user_by_email(email)
        if user:
            try:
                user.set_password(new_password)
                session.commit()
                return (True, "Senha atualizada com sucesso!")
            except ValueError as ve:
                return (False, f"Erro: {ve}")
        return (False, "Usuário não encontrado.")

    def save_verification_code(self, email, code):
        user = self.get_user_by_email(email)
        if user:
            user.verification_code = code
            session.commit()

    def check_verification_code(self, email, code):
        user = self.get_user_by_email(email)
        return user and user.verification_code == code
