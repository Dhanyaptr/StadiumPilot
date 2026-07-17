import re

from services.navigation_service import NavigationService
from services.facility_service import FacilityService
from services.rules_service import RulesService
from services.accessibility_service import AccessibilityService


class ChatService:

    def __init__(self):

        self.navigator = NavigationService()
        self.facility = FacilityService()
        self.rules = RulesService()
        self.accessibility = AccessibilityService()

        # -------------------------
        # Session Memory
        # -------------------------
        self.sessions = {}

        # -------------------------
        # Parking IDs
        # -------------------------
        self.parking_ids = [
            parking["parking_id"].upper()
            for parking in self.navigator.data["parking"]
        ]

        # -------------------------
        # Navigation Keywords
        # -------------------------
        self.navigation_keywords = [
            "section",
            "seat",
            "parking",
            "park",
            "gate",
            "entrance",
            "navigate",
            "navigation",
            "direction",
            "directions",
            "how do i get",
            "where is section",
            "take me"
        ]

        # -------------------------
        # Restroom Keywords
        # -------------------------
        self.restroom_keywords = [
            "restroom",
            "toilet",
            "washroom",
            "bathroom"
        ]

        # -------------------------
        # Food Keywords
        # -------------------------
        self.food_keywords = [
            "food",
            "eat",
            "hungry",
            "restaurant",
            "snack",
            "veg",
            "vegetarian",
            "non veg",
            "non-veg",
            "vegan",
            "pizza",
            "burger",
            "coffee",
            "tea",
            "drink",
            "juice"
        ]

        # -------------------------
        # Medical Keywords
        # -------------------------
        self.medical_keywords = [
            "medical",
            "doctor",
            "first aid",
            "clinic",
            "emergency",
            "hospital"
        ]

        # -------------------------
        # Merchandise Keywords
        # -------------------------
        self.merchandise_keywords = [
            "merchandise",
            "shop",
            "store",
            "jersey",
            "souvenir",
            "gift"
        ]

        # -------------------------
        # Stadium Rules
        # -------------------------
        self.rule_keywords = {

            "outside_food": [
                "outside food",
                "bring food",
                "food allowed"
            ],

            "camera": [
                "camera",
                "dslr",
                "photography"
            ],

            "smoking": [
                "smoking",
                "vaping",
                "cigarette"
            ],

            "bags": [
                "bag",
                "backpack",
                "luggage"
            ],

            "reentry": [
                "reentry",
                "re-entry",
                "leave and come back"
            ],

            "pets": [
                "pet",
                "dog",
                "cat",
                "service animal"
            ]

        }

        # -------------------------
        # Accessibility
        # -------------------------
        self.accessibility_keywords = {

            "wheelchair": [
                "wheelchair",
                "disabled",
                "mobility"
            ],

            "accessible_restroom": [
                "accessible restroom",
                "wheelchair restroom"
            ],

            "elevator": [
                "elevator",
                "lift"
            ],

            "hearing": [
                "hearing",
                "hearing aid",
                "assistive listening"
            ]

        }

    def process_message(self, session_id, message):

        # -------------------------------------------------
        # Create Session
        # -------------------------------------------------

        if session_id not in self.sessions:

            self.sessions[session_id] = {
                "parking": None,
                "section": None,
                "awaiting": None
            }

        session = self.sessions[session_id]

        message_lower = message.lower()

        # -------------------------------------------------
        # Continue Previous Conversation
        # -------------------------------------------------

        if session["awaiting"] == "parking":

            for pid in self.parking_ids:

                if re.search(rf"\b{re.escape(pid)}\b", message, re.IGNORECASE):

                    session["parking"] = pid
                    session["awaiting"] = None
                    break

        elif session["awaiting"] == "section":

            sec = re.search(r"\b\d{3}\b", message)

            if sec:

                session["section"] = sec.group()
                session["awaiting"] = None

        # -------------------------------------------------
        # Stadium Rules
        # -------------------------------------------------

        for topic, keywords in self.rule_keywords.items():

            if any(keyword in message_lower for keyword in keywords):

                return {
                    "status": "rule",
                    "topic": topic,
                    "rule": self.rules.get_rule(topic)
                }

        # -------------------------------------------------
        # Accessibility
        # -------------------------------------------------

        for topic, keywords in self.accessibility_keywords.items():

            if any(keyword in message_lower for keyword in keywords):

                if topic == "wheelchair":

                    return {
                        "status": "accessibility",
                        "facility_type": topic,
                        "facility": self.accessibility.get_wheelchair()
                    }

                elif topic == "accessible_restroom":

                    return {
                        "status": "accessibility",
                        "facility_type": topic,
                        "facility": self.accessibility.get_restroom()
                    }

                elif topic == "elevator":

                    return {
                        "status": "accessibility",
                        "facility_type": topic,
                        "facility": self.accessibility.get_elevator()
                    }

                elif topic == "hearing":

                    return {
                        "status": "accessibility",
                        "facility_type": topic,
                        "facility": self.accessibility.get_hearing()
                    }
        # -------------------------------------------------
        # Navigation Intent
        # -------------------------------------------------

        parking = None

        for pid in self.parking_ids:
            if re.search(rf"\b{re.escape(pid)}\b", message, re.IGNORECASE):
                parking = pid
                break

        section = re.search(r"\b\d{3}\b", message)

        if parking:
            session["parking"] = parking

        if section:
            session["section"] = section.group()

        is_navigation_query = (
            any(keyword in message_lower for keyword in self.navigation_keywords)
            or parking is not None
            or section is not None
            or session["awaiting"] is not None
        )

        if is_navigation_query:

            if session["parking"] is None:

                session["awaiting"] = "parking"

                if session["section"] is not None:
                    reply = (
                        f"Sure! I know you're heading to Section "
                        f"{session['section']}. Which parking lot are you parked in?"
                    )
                else:
                    reply = "Sure! Which parking lot are you parked in?"

                return {
                    "status": "need_parking",
                    "reply": reply
                }

            if session["section"] is None:

                session["awaiting"] = "section"

                return {
                    "status": "need_section",
                    "reply": (
                        f"Great! I have your parking location as "
                        f"{session['parking']}. Which section are you trying to reach?"
                    )
                }
            print("Session:", session)
            route = self.navigator.find_navigation(
                session["parking"],
                session["section"]
            )

            if "error" not in route:
                session["parking"] = None
                session["section"] = None
                session["awaiting"] = None

            return route
        # -------------------------------------------------
        # Facilities
        # -------------------------------------------------

        if any(word in message_lower for word in self.restroom_keywords):

            return {
                "status": "facility",
                "facility_type": "restroom",
                "facility": self.facility.get_restroom()
            }

        if any(word in message_lower for word in self.food_keywords):

            return {
                "status": "facility",
                "facility_type": "food",
                "facility": self.facility.get_food_court()
            }

        if any(word in message_lower for word in self.medical_keywords):

            return {
                "status": "facility",
                "facility_type": "medical",
                "facility": self.facility.get_medical()
            }

        if any(word in message_lower for word in self.merchandise_keywords):

            return {
                "status": "facility",
                "facility_type": "merchandise",
                "facility": self.facility.get_merchandise()
            }
        
        return {
            "status": "unknown",
            "reply": (
                "I'm sorry, I can only assist with stadium-related questions such as "
                "navigation, food courts, restrooms, medical assistance, "
                "merchandise, stadium rules, and accessibility."
            )
        }
        