import requests
import executor as exc

def send_message():
    config = exc.get_telegram_config()
    print(config)
    print("printed!")