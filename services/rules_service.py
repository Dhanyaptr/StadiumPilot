from services.dataloader import DataLoader


class RulesService:

    def __init__(self):

        loader = DataLoader()

        self.rules = loader.load_json("rules.json")

    def get_rule(self, topic):

        return self.rules.get(topic)