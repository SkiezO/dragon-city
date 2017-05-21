from app.main.src.GameManagement.Models import Offer
from app.main.src.GameManagement.Repositories import OfferRepository


class OfferService:
    offer_repository: OfferRepository = OfferRepository()

    def insert(self, action: Offer):
        return self.offer_repository.insert(action)

    def get_by_user_id(self, user_id):
        return self.offer_repository.get_by_user_id(user_id)