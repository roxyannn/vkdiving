import requests
import time
import threading
import random

TOKEN = "vk1.a.NpKmjOcxJbGbDJusuJvp7B5UF1RmcNxlT7rrkgp34Z5gnndkPHmak0cd41MS-hMnEROVDek9chaGqRFmS_dcIMI_lZAWR5shvsldPLysegGaCiq3yyYf44TywtLIfwkuv8JDM0x8ZiAj-LG0WA0Mdx8KunrOKZyYAoS6oq9oytbpFd3qUXYzdlsH1Aw5j8bJW5aPJaCnpsJ5XW1UUc7_xQ"
CHAT_ID = 2000000353
API_VERSION = "5.199"

# payload кнопки "Подводное плавание"
MANUAL_PAYLOAD = '{"button":"daiving"}'

def send_message(text=".", payload=None):
    url = "https://api.vk.com/method/messages.send"
    params = {
        "access_token": TOKEN,
        "v": API_VERSION,
        "peer_id": CHAT_ID,
        "random_id": random.randint(1, 2**63-1),
        "message": text
    }
    if payload:
        params["payload"] = payload
    r = requests.post(url, params=params).json()
    print("send_message response:", r)
    return r

def diving_loop():
    while True:
        # 1) пишем "дайвинг"
        send_message("дайвинг")
        time.sleep(2)
        # 2) "жмём" кнопку Подводное плавание
        send_message(".", payload=MANUAL_PAYLOAD)
        # 3) ждём 10 минут
        time.sleep(605)

threading.Thread(target=diving_loop, daemon=True).start()

while True:
    time.sleep(1)
