from services.dataloader import DataLoader


class FacilityService:

    def __init__(self):

        loader = DataLoader()

        self.data = loader.load_json("facilities.json")

    def get_restroom(self):

        return self.data["restrooms"][0]

    def get_food_court(self):

        return self.data["food_courts"][0]

    def get_medical(self):

        return self.data["medical"][0]

    def get_merchandise(self):

        return self.data["merchandise"][0]