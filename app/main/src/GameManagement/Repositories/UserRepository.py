from app.main.src.GameManagement.Models import User
from app.main.src.GameManagement.Repositories import Repository


class UserRepository(Repository):
    def __init__(self):
        super().__init__(User)
