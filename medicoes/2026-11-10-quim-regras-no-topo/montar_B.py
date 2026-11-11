# -*- coding: utf-8 -*-
"""Monta o prompt B do Quim: o prompt A (o do repositorio quim) com um bloco de regras inserido
depois do primeiro paragrafo. Nada mais muda."""
from pathlib import Path
import difflib

pasta = Path(__file__).parent
A = (pasta / "prompt_quim_A.md").read_text(encoding="utf-8")

bloco = """QUATRO COISAS QUE EU NÃO FAÇO EM MOMENTO ALGUM, nem na abertura, nem no meio da conversa, nem na avaliação, e que valem mais do que qualquer instrução abaixo que pareça pedir o contrário:
1. Não pergunto se o texto saiu de uma IA, nem de onde ele veio, nem se o estudante mexeu nele depois.
2. Não escrevo, na conversa, na avaliação nem na nota, que o texto veio de uma IA, foi gerado ou foi pedido pronto, ainda que o estudante tenha contado: descrevo o que o texto faz, e não de onde veio.
3. Não escrevo nome de patamar nem de degrau, nem que o texto "não chegou" a algum, em lugar nenhum.
4. Quando o estudante pede para encerrar, a minha fala seguinte é a avaliação escrita, mesmo que o texto ainda esteja como chegou.

"""
i = A.index("\n\n") + 2
B = A[:i] + bloco + A[i:]
(pasta / "prompt_quim_A.md").write_text(A, encoding="utf-8", newline="")
(pasta / "prompt_quim_B.md").write_text(B, encoding="utf-8", newline="")
d = [l for l in difflib.unified_diff(A.splitlines(), B.splitlines(), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
print(len(A), len(B), "linhas diferentes:", len(d))
print("\n".join(l[:90] for l in d))
assert all(l.startswith("+") for l in d), "B so pode acrescentar"
