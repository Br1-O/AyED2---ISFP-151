from datetime import datetime

def log_info(message: str):
    print(f"[INFO] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")

def log_warn(message: str):
    print(f"[WARN] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")

def log_error(message: str):
    print(f"[ERROR] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")
