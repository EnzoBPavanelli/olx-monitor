import requests

TELEGRAM_TOKEN = "7753035599:AAFPRQ-fI-7uRxwy8P_P_zdNDQFFkP_s5Fc"
TELEGRAM_CHAT_ID = "8140693630"

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
