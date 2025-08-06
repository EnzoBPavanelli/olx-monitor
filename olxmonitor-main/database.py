import sqlite3

def criar_banco():
    conn = sqlite3.connect("anuncios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anuncios (
            list_id TEXT PRIMARY KEY,
            titulo TEXT,
            preco REAL,
            palavra_chave TEXT,
            data TEXT,
            link TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir_anuncio(anuncio):
    conn = sqlite3.connect("anuncios.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO anuncios (list_id, titulo, preco, palavra_chave, data, link)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            anuncio["list_id"],
            anuncio["titulo"],
            anuncio["preco"],
            anuncio["palavra_chave"],
            anuncio["data"],
            anuncio["link"]
        ))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # já foi inserido
    finally:
        conn.close()
