import asyncio
import aiohttp
import re
import json
from pathlib import Path

# Configurações
timeout_seconds = 10          # Tempo máximo de espera por requisição
max_concurrency = 20         # Máximo de requisições simultâneas
pattern = re.compile(r'"merchantkey"\s*:\s*"([^\"]+)"')
site_file = Path('site.txt')
output_file = Path('found_keys.json')

async def fetch_and_search(session: aiohttp.ClientSession, url: str, sem: asyncio.Semaphore, results: list):
    """
    Faz requisição GET no URL, procura pelo padrão de merchantkey e registra resultados.
    """
    async with sem:
        target = url if url.startswith(('http://', 'https://')) else f'http://{url}'
        try:
            async with session.get(target) as response:
                text = await response.text()
                match = pattern.search(text)
                if match:
                    key = match.group(1)
                    print(f"✓ {url}: {key}")
                    results.append({'site': url, 'merchantkey': key})
                else:
                    print(f"✗ {url}")
        except Exception as e:
            print(f"⚠ {url}: {e}")

async def main():
    sem = asyncio.Semaphore(max_concurrency)
    conn = aiohttp.TCPConnector(limit=max_concurrency)
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)
    results = []

    async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
        urls = [line.strip() for line in site_file.read_text().splitlines() if line.strip()]
        tasks = [fetch_and_search(session, url, sem, results) for url in urls]
        await asyncio.gather(*tasks)

    if results:
        with output_file.open('w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n=> {len(results)} sites com merchantkey salvos em '{output_file}'")
        # Exibe tabela simples
        site_col_width = max(len(r['site']) for r in results) + 2
        key_col_width = max(len(r['merchantkey']) for r in results) + 2
        header = f"{'Site'.ljust(site_col_width)} | {'MerchantKey'.ljust(key_col_width)}"
        separator = '-' * len(header)
        print(separator)
        print(header)
        print(separator)
        for r in results:
            print(f"{r['site'].ljust(site_col_width)} | {r['merchantkey'].ljust(key_col_width)}")
        print(separator)
    else:
        print("\n=> Nenhum merchantkey encontrado.")

if __name__ == '__main__':
    asyncio.run(main())

# Dependências:
# pip install aiohttp
