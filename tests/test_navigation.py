from services.navigation_service import NavigationService

navigator = NavigationService()

route = navigator.find_navigation("50A", "110")

print(route)