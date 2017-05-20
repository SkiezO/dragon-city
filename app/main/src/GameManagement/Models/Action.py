from app.main.src.GameManagement.Models import User
from app.main.src.GameManagement.Models.IModel import IModel


class Action(IModel):
    id: int
    user: User
    name: str
