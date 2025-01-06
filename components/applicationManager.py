import requests
from enums.mode import Mode

class ApplicationManager:
    def __init__(self):
        self.start()

    def start(self):
        print("Welcome to application layer!")

    def modeManager(self):
        try:
            response = requests.get("http://www.google.com", timeout=5)
            if response.status_code == 200:
                return Mode.ONLINE
        except requests.ConnectionError:
            pass

        return Mode.OFFLINE

