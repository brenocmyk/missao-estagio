import os
import requests
from dotenv import load_dotenv

load_dotenv()


def enviar_msg(numero, mensagem):

    instance = os.getenv("ZAPI_INSTANCE")
    token = os.getenv("ZAPI_TOKEN")

    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"

    payload = {
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(
        url,
        json=payload
    )

    return response.json()