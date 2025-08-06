import requests

TELEGRAM_TOKEN = "COLE AQUI SEWU TOKEN"
TELEGRAM_CHAT_ID = "COLE AQUI SEU CHAT ID"

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("❌ Erro ao enviar para o Telegram:", e)

