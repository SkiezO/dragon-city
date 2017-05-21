from app.main.src.GameManagement.Models import GameAction
from app.main.src.GameManagement.Repositories import Repository


class GameActionRepository(Repository):
    def __init__(self):
        super().__init__(GameAction)
