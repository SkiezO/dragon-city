from app.main.src.GameManagement.Models import User, Action, Order


class ReportLineToDragonCityAdapter:
    def __init__(self, columns: list):
        self.user = User()
        self.user.id = str(columns[0])
        self.user.classification = str(columns[1])
        self.action = Action()
        self.action.user = self.user
        self.action.name = str(columns[2])
        self.order = Order()
        self.order.user = self.user
        self.order.action = self.action
        self.order.amount = int(columns[3])

