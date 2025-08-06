from filters import FILTROS
import re

def normalizar(texto):
    return texto.lower().replace(" ", "").replace("-", "")

def tratar_preco(valor):
    try:
        return float(re.sub(r"[^\d,]", "", valor).replace(",", "."))
    except:
        return None

def filtrar_anuncio(anuncio):
    titulo = anuncio.get("title", "")
    preco_str = anuncio.get("price", "")
    preco = tratar_preco(preco_str)

    if preco is None:
        return None

    titulo_normalizado = normalizar(titulo)

    for palavra, faixa in FILTROS.items():
        if palavra in titulo_normalizado:
            preco_min = faixa.get("min", 0)
            preco_max = faixa.get("max", float("inf"))
            if preco_min <= preco <= preco_max:
                return {
                    "list_id": anuncio.get("listId"),
                    "titulo": titulo,
                    "preco": preco,
                    "palavra_chave": palavra,
                    "data": anuncio.get("date"),
                    "link": anuncio.get("url", "")
                }

    return None
