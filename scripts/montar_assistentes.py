# -*- coding: utf-8 -*-
"""Monta assistentes/<nome>.md a partir da fonte de cada prompt, sem redigitar nada.

Quim e Ana: prompt_portatil.md dos repositorios quim e ana (via `gh api`).
Miguel: o texto que o artifact dele traz num <script id="dados" type="application/json">;
quem roda passa o index.html salvo do artifact em --miguel.

    python scripts/montar_assistentes.py --miguel caminho/index.html

Cada arquivo gerado abre com uma linha de origem e data. Nao edite os arquivos
gerados: a fonte e o repositorio ou o artifact do assistente, e este programa os recopia.
"""
import argparse, base64, datetime, json, re, subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOJE = datetime.date.today().isoformat()


def do_github(repo):
    saida = subprocess.run(
        ["gh", "api", f"repos/AlexandreAraujoCosta/{repo}/contents/prompt_portatil.md", "--jq", ".content"],
        capture_output=True, check=True).stdout
    return base64.b64decode(saida).decode("utf-8")


def do_artifact(caminho):
    s = Path(caminho).read_text(encoding="utf-8")
    m = re.search(r'<script id="dados" type="application/json">(.*?)</script>', s, re.S)
    if not m:
        sys.exit("nao achei o <script id=\"dados\"> no arquivo do Miguel")
    texto = json.loads(m.group(1))
    if not isinstance(texto, str) or len(texto) < 1000:
        sys.exit("o conteudo de dados nao parece o prompt do Miguel")
    return texto


def grava(nome, texto, origem):
    cab = f"<!-- Origem: {origem}. Copiado em {HOJE}. Nao edite: rode scripts/montar_assistentes.py. -->\n\n"
    (RAIZ / "assistentes").mkdir(exist_ok=True)
    (RAIZ / "assistentes" / f"{nome}.md").write_text(cab + texto.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"{nome}: {len(texto)} caracteres")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--miguel", help="index.html salvo do artifact do Miguel")
    a = ap.parse_args()
    grava("quim", do_github("quim"), "repositorio AlexandreAraujoCosta/quim, prompt_portatil.md")
    grava("ana", do_github("ana"), "repositorio AlexandreAraujoCosta/ana, prompt_portatil.md")
    if a.miguel:
        grava("miguel", do_artifact(a.miguel), "artifact Miguel (https://claude.ai/artifact/8SSdumvbmfNBSh8RgXcqYD)")
    else:
        print("miguel: nao gerado (passe --miguel)")


if __name__ == "__main__":
    main()
