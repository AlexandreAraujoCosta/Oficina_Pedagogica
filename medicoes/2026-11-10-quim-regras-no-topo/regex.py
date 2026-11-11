# -*- coding: utf-8 -*-
"""Medidas 1 a 4 por regex, sobre as transcricoes com codigo. Com controle positivo e negativo."""
import re
from pathlib import Path

pasta = Path(__file__).parent
chave = {}
for l in (pasta / "CHAVE_CODIGOS.txt").read_text(encoding="utf-8").splitlines():
    c, aid, braco, _ = l.split()
    chave[c] = braco


def turnos(t):
    return [(m.group(1), m.group(2).strip()) for m in re.finditer(r"\[(ASSISTENTE|ESTUDANTE)\]\n(.*?)(?=\n\n\[(?:ASSISTENTE|ESTUDANTE)\]\n|\Z)", t, re.S)]


RE_M1 = re.compile(r"[^.!?\n]*\b(IA|inteligência artificial|ChatGPT)\b[^.!?\n]*\?", re.I)
RE_M2 = re.compile(r"\bIA\b|ChatGPT|inteligência artificial|\bgerad[oa]s?\b|pedido pronto|pedido inteiro", re.I)
RE_M3 = re.compile(r"patamar|degrau", re.I)


def medidas(txt):
    tur = turnos(txt)
    ass = [t for r, t in tur if r == "ASSISTENTE"]
    primeira, ultima = ass[0], ass[-1]
    aval = ultima.split("**Avaliação**", 1)[1] if "**Avaliação**" in ultima else ""
    return {
        "M1": bool(RE_M1.search(primeira)),
        "M2": bool(RE_M2.search(aval)),
        "M3": any(RE_M3.search(t) for t in ass),
        "M4": "**Avaliação**" in ultima,
    }


# controles
pos = "[ASSISTENTE]\nEsse texto saiu de uma IA e você o trouxe sem mexer?\n\n[ESTUDANTE]\n(Estudante.) oi\n\n[ASSISTENTE]\nO texto não chegou ao patamar. **Avaliação** O rascunho veio de uma IA."
neg = "[ASSISTENTE]\nO relógio atrasado é um detalhe vivo. O que ele diz do tio?\n\n[ESTUDANTE]\n(Estudante.) oi\n\n[ASSISTENTE]\n**Avaliação** O texto tem um relógio."
print("controle positivo:", medidas(pos))
print("controle negativo:", medidas(neg))
assert medidas(pos) == {"M1": True, "M2": True, "M3": True, "M4": True}
assert medidas(neg) == {"M1": False, "M2": False, "M3": False, "M4": True}

res = {}
for c in sorted(chave):
    res[c] = medidas((pasta / "transcricoes" / f"{c}.txt").read_text(encoding="utf-8"))
for b in ("A", "B"):
    cs = [c for c in sorted(chave) if chave[c].startswith(b)]
    print(f"\nBraço {b}: {len(cs)} conversas")
    for m in ("M1", "M2", "M3", "M4"):
        n = sum(res[c][m] for c in cs)
        print(f"  {m}: {n} de {len(cs)}")
print("\npor conversa:")
for c in sorted(chave):
    print(c, chave[c], res[c])
