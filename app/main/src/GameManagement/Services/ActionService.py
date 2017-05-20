from app.main.src.GameManagement.Models import Action
from app.main.src.GameManagement.Repositories import ActionRepository


class ActionService:
    action_repository: ActionRepository = ActionRepository()

    def get(self, action: Action):
        return self.action_repository.get(action)

