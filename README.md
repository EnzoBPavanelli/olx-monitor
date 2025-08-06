
# OLX_WebScraping – Monitorador de Preços com Alerta via Telegram

Este projeto realiza web scraping na OLX com o objetivo de monitorar anúncios de câmeras novas e usadas, enviando alertas em tempo real via Telegram. Foi desenvolvido com foco em uso pessoal para facilitar a busca por boas oportunidades de compra e venda no mercado de fotografia.

## Objetivo

Criar um sistema automatizado de monitoramento de produtos na OLX que:

- Filtra anúncios com base em palavras-chave e faixa de preço
- Envia notificações via Telegram sempre que um novo anúncio compatível é encontrado
- Permite fácil personalização para outros produtos além de câmeras

## Tecnologias e Ferramentas

- Python 3
- requests e BeautifulSoup para web scraping
- API do Telegram para envio de mensagens
- Estrutura modular e fácil de adaptar

## Estrutura do Projeto

olxmonitor-main/

├── main2.py               
├── filters.py              
├── notifier.py     
├── parser.py         
├── telegram_bot.py             
├── enviados.jason      
├── requirements.txt 

## Como Funciona

1. O script `main2.py` realiza buscas periódicas na OLX com base nos filtros definidos.
2. Novos anúncios compatíveis são extraídos e comparados com os que já foram enviados.
3. Quando um novo anúncio é detectado, ele é enviado como mensagem via Telegram.
4. O sistema evita repetições usando o arquivo `enviados.json`.

## Como Usar

1. Clone este repositório.
2. Instale as dependências:
     pip install -r requirements.txt
3. Configure o token e ID do chat no arquivo `telegram_bot.py`.
4. Edite os filtros desejados no arquivo `filters.py`.
5. Execute o script principal:
     python main2.py

O monitoramento será executado em ciclos e alertará via Telegram conforme os filtros definidos.

## Personalização

Você pode adaptar este sistema para qualquer tipo de produto, ajustando:

- As palavras-chave e faixa de preços em `filters.py`
- O formato de envio das mensagens em `notifier.py`

## Status

Projeto funcional e utilizado regularmente para monitorar o mercado de câmeras fotográficas na OLX. Em constante evolução conforme necessidades pessoais.

## Licença

Uso pessoal. Todos os direitos reservados ao autor.

## Contato

Enzo Pavanelli  
LinkedIn: https://www.linkedin.com/in/enzo-brito-pavanelli-269290256/
GitHub: https://github.com/EnzoBPavanelli
