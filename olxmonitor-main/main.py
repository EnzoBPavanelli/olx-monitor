import json
import os
from parsel import Selector
import cloudscraper
from datetime import datetime
import time
from parser import filtrar_anuncio
from telegram_bot import enviar_telegram
import re
ARQUIVO_ENVIADOS = "enviados.json"
INTERVALO_MINUTOS = 1

def escapar_markdown(texto):
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', texto)
# Função para carregar os listIds enviados do arquivo
def carregar_ids_enviados():
    if os.path.exists(ARQUIVO_ENVIADOS):
        with open(ARQUIVO_ENVIADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Função para salvar os listIds enviados no arquivo
def salvar_ids_enviados(ids):
    with open(ARQUIVO_ENVIADOS, "w", encoding="utf-8") as f:
        json.dump(ids, f)

# Carrega lista no início
listIds_enviados = carregar_ids_enviados()

def rodar_monitoramento():
    global listIds_enviados

    scraper = cloudscraper.create_scraper()
    url = "https://www.olx.com.br/cameras-e-filmadoras?q=sony&sf=1"
    r = scraper.get(url)
    response = Selector(text=r.text)

    try:
        html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
        anuncios = html.get('props', {}).get('pageProps', {}).get('ads', [])
    except Exception as e:
        print(f"❌ Erro ao carregar anúncios: {e}")
        return

    for a in anuncios:
        list_id = a.get("listId")

        if not list_id or list_id in listIds_enviados:
            continue  # já enviado ou inválido

        dado = filtrar_anuncio(a)
        if dado:
            dado["data"] = datetime.fromtimestamp(dado["data"]).strftime("%d/%m/%Y %H:%M")
            mensagem = (
                f"*📸 {escapar_markdown(dado['titulo'])}*\n"
                f"💸 R\\$ {dado['preco']}\n"
                f"🔍 Palavra-chave: {escapar_markdown(dado['palavra_chave'])}\n"
                f"🕓 {dado['data']}\n"
                f"{dado['link']}"
            )
            print(dado)

            try:
                enviar_telegram(mensagem)
                print(f"✔️ Enviado: {dado['titulo']} - R${dado['preco']}")
                listIds_enviados.append(list_id)
                salvar_ids_enviados(listIds_enviados)
            except Exception as e:
                print(f"❌ Erro ao enviar para Telegram: {e}")
    print("Nada encontrado")

# Looping de execução
print(f"🟢 Monitoramento iniciado. Rodando a cada {INTERVALO_MINUTOS} minutos...")
a=0
while True:
    rodar_monitoramento()
    print("Ativo por ",a,"minutos")
    time.sleep(INTERVALO_MINUTOS * 60)
    a+=1
