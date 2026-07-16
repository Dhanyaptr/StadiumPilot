from services.navigation_service import NavigationService
from services.prompt_builder import PromptBuilder

navigator = NavigationService()

route = navigator.find_navigation("50A", "110")
print(route)

prompt = PromptBuilder.build_navigation_prompt(route)

print(prompt)
