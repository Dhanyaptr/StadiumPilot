import json
from pathlib import Path


class DataLoader:
    def __init__(self):
        # backend/
        self.base_path = Path(__file__).resolve().parent.parent

        # backend/dataset/
        self.dataset_path = self.base_path / "dataset"

    def load_json(self, filename):
        file_path = self.dataset_path / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_all_data(self):
        return {
            "stadium": self.load_json("stadium.json"),
            "parking": self.load_json("parking.json"),
            "entrances": self.load_json("entrances.json"),
            "sections": self.load_json("sections.json"),
            "routes": self.load_json("routes.json"),
            "facilities": self.load_json("facilities.json"),
            "rules": self.load_json("rules.json"),
            "accessibility": self.load_json("accessibility.json"),
        }