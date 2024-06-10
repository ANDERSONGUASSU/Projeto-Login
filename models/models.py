import bcrypt
import re
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_URL


Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    verification_code = Column(String(6), nullable=False)

    def set_password(self, password):
        self.validate_password_strength(password)
        self.password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("utf-8")

    def check_password(self, password):
        if self.password is None:
            raise ValueError("A senha não está definida para este usuário")
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def validate_password_strength(self, password):
        if len(password) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres")
        if not re.search(r"[A-Z]", password):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula")
        if not re.search(r"[a-z]", password):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula")
        if not re.search(r"\d", password):
            raise ValueError("A senha deve conter pelo menos um dígito")
        if not re.search(r"[!@#$%^&*+-_=§¨¬¹²³£¢ªº`~;°(),.?/\":{}|<>]", password):
            raise ValueError("A senha deve conter pelo menos um caractere especial")

    def __repr__(self):
        return f"<User(nome={self.nome}, email={self.email})>"


Base.metadata.create_all(engine)
