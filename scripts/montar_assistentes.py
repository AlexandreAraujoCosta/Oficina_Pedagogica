# -*- coding: utf-8 -*-
"""Monta assistentes/<nome>.md a partir da PAGINA EM USO de cada assistente, sem redigitar nada.

A fonte e o texto que o estudante copia: o prompt da pagina publicada (artifact) de cada assistente. O arquivo
prompt_portatil.md dos repositorios quim e ana pode estar defasado em relacao a ela (em 10/11/2026 estava), e por
isso nao e mais usado aqui.

A pagina traz o prompt num <textarea id="prompt"> (Quim, Ana) ou num <script id="dados" type="application/json">
(Miguel). Quem roda passa o index.html salvo de cada artifact:

    python scripts/montar_assistentes.py --quim q.html --ana a.html --miguel m.html

Cada arquivo gerado abre com uma linha de origem e data. Nao edite os arquivos gerados.
"""
import argparse, datetime, html, json, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOJE = datetime.date.today().isoformat()

ORIGENS = {
    "quim": "pagina do Quim (https://claude.ai/artifact/YBpbYtMFFv3YMaDCmqhA4n)",
    "ana": "pagina da Ana (https://claude.ai/artifact/E1GN8k2cNaoHiZ7bTWPcdS)",
    "miguel": "pagina do Miguel (https://claude.ai/artifact/8SSdumvbmfNBSh8RgXcqYD)",
}


def prompt_da_pagina(caminho):
    s = Path(caminho).read_text(encoding="utf-8")
    m = re.search(r'<textarea id="prompt"[^>]*>(.*?)</textarea>', s, re.S)
    if m:
        texto = html.unescape(m.group(1))
    else:
        m = re.search(r'<script id="dados" type="application/json">(.*?)</script>', s, re.S)
        if not m:
            sys.exit(f"nao achei o prompt em {caminho}: nem textarea#prompt nem script#dados")
        texto = json.loads(m.group(1))
    if not isinstance(texto, str) or len(texto) < 10000:
        sys.exit(f"o texto achado em {caminho} nao parece um prompt completo")
    return texto.strip()


def grava(nome, texto):
    cab = f"<!-- Origem: {ORIGENS[nome]}. Copiado em {HOJE}. Nao edite: rode scripts/montar_assistentes.py. -->\n\n"
    (RAIZ / "assistentes").mkdir(exist_ok=True)
    (RAIZ / "assistentes" / f"{nome}.md").write_text(cab + texto + "\n", encoding="utf-8", newline="\n")
    print(f"{nome}: {len(texto)} caracteres")


def main():
    ap = argparse.ArgumentParser()
    for n in ("quim", "ana", "miguel"):
        ap.add_argument(f"--{n}", help=f"index.html salvo do artifact do {n.capitalize()}")
    a = ap.parse_args()
    feito = False
    for n in ("quim", "ana", "miguel"):
        caminho = getattr(a, n)
        if caminho:
            grava(n, prompt_da_pagina(caminho))
            feito = True
    if not feito:
        sys.exit("passe ao menos um de --quim, --ana, --miguel")


if __name__ == "__main__":
    main()
