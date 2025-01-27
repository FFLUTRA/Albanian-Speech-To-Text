from abc import ABC, abstractmethod
from enums.level import LEVEL
from components.user import User

class UserDao(ABC):

    @abstractmethod
    def add_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def update_email(self, user: User, new_email: str) -> bool:
        pass

    @abstractmethod
    def reset_password(self, user: User, new_password: str) -> bool:
        pass

    def update_security_level(self, user: User, new_level: LEVEL) -> bool:
        pass

    @abstractmethod
    def delete_account(self, user: User) -> bool:
        pass

    @abstractmethod
    def get_user_details(self, user: User) -> User:
        pass