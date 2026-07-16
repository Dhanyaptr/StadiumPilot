from pydantic import BaseModel


class NavigationRequest(BaseModel):
    parking_id: str
    section_id: str

class ChatRequest(BaseModel):
    session_id: str
    message: str