from app.main.src.GameManagement.Models import Action
from app.main.src.GameManagement.Repositories import Repository


class ActionRepository(Repository):
    def __init__(self):
        super().__init__(Action)
