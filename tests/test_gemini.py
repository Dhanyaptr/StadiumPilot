import os
from dotenv import load_dotenv

load_dotenv()

from services.navigation_service import NavigationService
from services.prompt_builder import PromptBuilder
from services.gemini_service import GeminiService

# Replace with your own API key
API_KEY = os.getenv("GROQ_API_KEY")

navigator = NavigationService()

route = navigator.find_navigation("50A", "110")

prompt = PromptBuilder.build_navigation_prompt(route)

gemini = GeminiService(API_KEY)

response = gemini.generate_response(prompt)

print(response)