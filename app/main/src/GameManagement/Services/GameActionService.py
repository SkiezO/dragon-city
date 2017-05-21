from app.main.src.GameManagement.Models import GameAction
from app.main.src.GameManagement.Repositories import GameActionRepository


class GameActionService:
    game_action_repository: GameActionRepository = GameActionRepository()

    def insert(self, action: GameAction):
        return self.game_action_repository.insert(action)

    def get_by_user_id(self, user_id):
        return self.game_action_repository.get_by_user_id(user_id)