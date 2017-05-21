from app.main.src.GameManagement.Models import GameAction
from app.main.src.GameManagement.Repositories import ActionRepository


class ActionService:
    action_repository: ActionRepository = ActionRepository()

    def insert(self, action: GameAction):
        return self.action_repository.insert(action)

    def get_by_user_id(self, user_id):
        return self.action_repository.get_by_user_id(user_id)