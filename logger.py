from datetime import datetime

class KeyLogger:
    def __init__(self):
        self.logs = []
        self.is_logging = False

    def start(self):
        self.is_logging = True

    def stop(self):
        self.is_logging = False

    def log_key(self, event):
        if self.is_logging:
            if event.char:
                key = event.char
                self.logs.append(f"Key: {key}")
            else:
                spkey=event.keysym
                self.logs.append(f"Special Key: {spkey}")
            
