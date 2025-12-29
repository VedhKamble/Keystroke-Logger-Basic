from datetime import datetime
import os

def save_logs(logs):
    if not logs:
        return None

    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logs/keystrokes_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Keystroke Logging Time: " + timestamp + "\n")
        for line in logs:
            file.write(line + "\n")

    return filename
