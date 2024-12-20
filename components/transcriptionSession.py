from components.mode import Mode

class TranscriptionSession:
    def __init__(self, mode: Mode):
        self.start_time = None
        self.end_time = None
        self.mode = mode