from services.dataloader import DataLoader


class NavigationService:

    def __init__(self):
        loader = DataLoader()
        self.data = loader.load_all_data()

    def find_navigation(self, parking_id, section_id):

        # ---------- Find Parking ----------
        parking = next(
            (
                p
                for p in self.data["parking"]
                if p["parking_id"] == parking_id
            ),
            None,
        )

        if not parking:
            return {"error": "Parking lot not found"}

        # ---------- Find Section ----------
        section = next(
            (
                s
                for s in self.data["sections"]
                if s["section_id"] == section_id
            ),
            None,
        )

        if not section:
            return {"error": "Section not found"}

        # ---------- Build Response ----------
        return {

            "parking_name": parking["parking_name"],

            "recommended_entrance": parking["recommended_entrance"],

            "nearest_gate": section["nearest_gate"],

            "section_id": section["section_id"],

            "walking_time": parking["walking_time"]

}