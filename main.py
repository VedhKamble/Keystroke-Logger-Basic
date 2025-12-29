import tkinter as tk
from logger import KeyLogger
from storage import save_logs

def main():
    print("Educational Keylogger Project")
    print("Keystrokes are logged ONLY inside this application.")

    logger = KeyLogger()

    root = tk.Tk()
    root.title("Educational Keylogger (Consent-Based)")
    root.geometry("500x300")

    label = tk.Label(
        root,
        text="Type inside this window.\nLogging is active ONLY with your consent.",
        fg="red"
    )
    label.pack(pady=10)

    text_box = tk.Text(root, height=8)
    text_box.pack()
    text_box.bind("<KeyPress>", logger.log_key)

    def start_logging():
        logger.start()
        status.config(text="Logging Started", fg="green")

    def stop_logging():
        logger.stop()
        file = save_logs(logger.logs)
        status.config(
            text=f"Logging Stopped. Saved to {file}",
            fg="blue"
        )

    tk.Button(root, text="Start Logging", command=start_logging).pack(pady=5)
    tk.Button(root, text="Stop & Save Logs", command=stop_logging).pack(pady=5)

    status = tk.Label(root, text="Logging Inactive")
    status.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
