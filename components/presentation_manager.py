import requests
from enums.mode import Mode

class PresentationManager:
    def __init__(self):
        self.start()

    def start(self):
        print("Welcome to presentation layer!")

    def modeManager(self):
        try:
            response = requests.get("http://www.google.com", timeout=5)
            if response.status_code == 200:
                return Mode.ONLINE
        except requests.ConnectionError:
            pass

        return Mode.OFFLINE