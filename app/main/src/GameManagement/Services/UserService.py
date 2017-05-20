from app.main.src.GameManagement.Models.User import User
from app.main.src.GameManagement.Repositories import UserRepository


class UserService:
    user_repository: UserRepository = UserRepository()

    def get(self, user: User):
        return self.user_repository.get(user)

