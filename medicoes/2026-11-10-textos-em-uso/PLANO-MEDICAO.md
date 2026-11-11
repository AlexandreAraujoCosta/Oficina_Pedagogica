# Medição do texto em uso do Quim e da Ana (10/11/2026)

Escrito antes de rodar. Nenhum número abaixo é resultado.

**Por que esta rodada.** A medição de 10/11 sobre o Quim (`../2026-11-10-quim-regras-no-topo/`) usou o
`prompt_portatil.md` do repositório, que era mais antigo que a página em uso. Os "desvios" que ela contou eram, em
parte, instruções da cópia antiga. Esta rodada mede o texto que o estudante de fato copia: o da página de cada
assistente (`assistentes/quim.md`, 35.918 caracteres, e `assistentes/ana.md`, 53.857).

**O que se sabe do texto em uso** (conferido por busca nos arquivos): os dois proíbem perguntar se o texto saiu de uma
IA, proíbem nomear patamar na conversa e na avaliação, mandam que a fala seguinte ao pedido de encerrar seja a avaliação,
e proíbem escrever trecho no lugar do estudante.

**O que se mede**, uma conversa por unidade, sim ou não (a quinta é contagem):
1. a primeira fala pergunta se o texto saiu de uma IA, ou se o estudante mexeu nele depois;
2. a avaliação ou a nota dizem ou sugerem que o texto veio de uma IA, foi gerado ou pedido pronto;
3. alguma fala usa "patamar" ou "degrau", ou classifica o trabalho por nível;
4. depois do primeiro pedido de encerrar, a fala seguinte traz a avaliação;
5. afirmações da avaliação ou da nota que atribuem ao estudante iniciativa que a transcrição contradiz;
6. aspas na avaliação ou na nota (o texto do Quim e o da Ana proíbem citar o estudante).

**Como roda.** Chat simulado, sem ferramentas e sem `AGENTS.md`. Quatro conversas por assistente, o mesmo roteiro de
estudante nas quatro, rascunho sintético (um texto sobre "Teoria do Medalhão" para o Quim, um voto sobre o caso dos
exploradores de cavernas para a Ana). Os números 1 a 4 e 6 por expressão regular, com controle positivo e negativo; todas
as seis por leitor que não sabe a que assistente a transcrição pertence (códigos aleatórios).

**O que se espera, em número.** Como os dois textos já trazem as regras: medidas 1, 2 e 3 em no máximo uma de quatro por
assistente; medida 4 em quatro de quatro; medida 6 em no máximo uma de quatro. Para a medida 5, que as medições
anteriores mostraram falhar em sete de doze conversas, espero ao menos duas de quatro em cada assistente.

**O que mostraria que o texto em uso não faz o que diz.** Qualquer das medidas 1, 2 ou 3 em três ou mais de quatro conversas de
um assistente. Nesse caso o texto proíbe e o modelo faz, e o bloco de regras no começo (medido só na cópia antiga) passa a
ser candidato a teste sobre o texto em uso. Se a medida 5 ficar em uma ou nenhuma de quatro, a regra de conferir quem disse
primeiro, que o texto traz, funciona neste cenário.

**Limites.** Quatro conversas por assistente, um rascunho por assistente, um só modelo, estudante simulado por quem
escreveu o plano, agentes que herdam as instruções globais da máquina de quem roda. Nenhuma frequência.
