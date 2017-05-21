from app.main.src.GameManagement.Models.User import User
from app.main.src.GameManagement.Repositories import UserRepository


class UserService:
    user_repository: UserRepository = UserRepository()

    def get(self, user: User):
        return self.user_repository.get(user)

    def insert_or_update(self, user: User):
        return self.user_repository.insert_or_update(user)

    def get_by_id(self, id_value):
        return self.user_repository.get_by_id(id_value)

