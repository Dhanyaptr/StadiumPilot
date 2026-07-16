from services.dataloader import DataLoader


class AccessibilityService:

    def __init__(self):

        loader = DataLoader()

        self.data = loader.load_json("accessibility.json")

    def get_wheelchair(self):
        return self.data["wheelchair"]

    def get_restroom(self):
        return self.data["accessible_restroom"]

    def get_elevator(self):
        return self.data["elevator"]

    def get_hearing(self):
        return self.data["hearing_assistance"]