
# 🔍  MerchantKey Finder — Escaneador de Sites

Este projeto é uma ferramenta automatizada feita em Python para **escanear uma lista de sites** e **identificar a presença de chaves `merchantkey`** em seu conteúdo. A ideia surgiu e foi desenvolvida com apoio do ChatGPT, focando em desempenho, simplicidade e praticidade.

---

## 🚀 Funcionalidades

- ✅ Leitura automática de links de um arquivo `.txt`
- ⚡ Escaneamento assíncrono e rápido com `aiohttp` + `asyncio`
- 🔍 Busca eficiente por `merchantkey` em cada site
- 💾 Exportação dos resultados encontrados em JSON
- 📊 Exibição de resultados formatados no terminal

---

## 📦 Requisitos

- Python 3.7 ou superior
- Instalar as dependências com:

```bash
pip install aiohttp
```

---

## 📁 Como usar

1. Clone este repositório:

```bash
git clone https://github.com/Pugn0/Scan-MerchantKey.git
cd Scan-MerchantKey
```

2. Crie um arquivo chamado `site.txt` contendo os domínios que deseja escanear (um por linha):

```
rede.medsempre.com.br
google.com
outro-site.com
```

3. Execute o script:

```bash
python main.py
```

4. Os resultados aparecerão no terminal e também serão salvos no arquivo `found_keys.json`.

---

## 🎥 Demonstração

Confira o vídeo completo onde mostro como criei e uso essa automação com ajuda do ChatGPT:

👉 [Assista aqui](https://youtube.com/seu-video-aqui)

---

## 🧠 Tecnologias utilizadas

- Python
- aiohttp
- asyncio
- re (expressões regulares)
- ChatGPT (como assistente na criação do projeto)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, melhorar e compartilhar.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se quiser adicionar novas features ou melhorias, fique à vontade para abrir uma PR ou issue.

---

## 📬 Contato

Dúvidas, sugestões ou parcerias?  
Entre em contato via [Instagram](https://instagram.com/seuuser) ou [Telegram](https://t.me/seulink).
