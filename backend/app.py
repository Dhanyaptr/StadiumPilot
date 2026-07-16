from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import traceback

from models.request_models import NavigationRequest, ChatRequest
from services.navigation_service import NavigationService
from services.chat_service import ChatService
from services.prompt_builder import PromptBuilder
from services.groq_service import GroqService

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# ---------------------------------------------------
# FastAPI App
# ---------------------------------------------------

app = FastAPI(
    title="StadiumPilot AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Initialize Services
# ---------------------------------------------------

navigator = NavigationService()
chat_service = ChatService()
llm = GroqService(API_KEY)

# ===================================================
# Navigation API
# ===================================================

@app.post("/navigate")
def navigate(request: NavigationRequest):

    route = navigator.find_navigation(
        request.parking_id,
        request.section_id
    )

    if "error" in route:
        return route

    prompt = PromptBuilder.build_navigation_prompt(route)

    ai_response = llm.generate_response(prompt)

    return {
        "status": "success",
        "navigation": route,
        "reply": ai_response
    }


# ===================================================
# Chat API
# ===================================================

@app.post("/chat")
def chat(request: ChatRequest):

    try:

        result = chat_service.process_message(
            request.session_id,
            request.message
        )

        print(result)

        if result is None:
            return {
                "status": "error",
                "reply": "ChatService returned no response."
            }

        # ChatService already prepared a reply
        if "reply" in result:
            return result

        status = result.get("status")

        # Facility
        if status == "facility":

            prompt = PromptBuilder.build_facility_prompt(
            result,
            request.message
        )

        # Rules
        elif status == "rule":

            prompt = PromptBuilder.build_rule_prompt(result)

        # Accessibility
        elif status == "accessibility":

            prompt = PromptBuilder.build_accessibility_prompt(result)

        # Navigation (or any result without a status key)
        else:

            prompt = PromptBuilder.build_navigation_prompt(result)

        ai_response = llm.generate_response(prompt)
        print(repr(ai_response))

        return {
            "status": "success",
            "navigation": result if status is None else None,
            "reply": ai_response
        }

    except Exception:

        traceback.print_exc()

        return {
            "status": "error",
            "reply": "Sorry, something went wrong. Please try again."
        }