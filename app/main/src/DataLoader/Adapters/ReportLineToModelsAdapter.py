from app.main.src.GameManagement.Models import User, GameAction, Offer


class ReportLineToModelsAdapter:
    def __init__(self, columns: list):
        self.user = User()
        self.user.id = str(columns[0])
        self.user.classification = str(columns[1])
        self.game_action = GameAction()
        self.game_action.user = self.user
        self.game_action.name = str(columns[2])
        self.offer = Offer()
        self.offer.user = self.user
        self.offer.action = self.game_action
        self.offer.amount = int(columns[3])

