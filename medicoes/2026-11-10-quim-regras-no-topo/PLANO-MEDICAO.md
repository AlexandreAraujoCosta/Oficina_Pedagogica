# Rodada de medição do prompt do Quim (10/11/2026)

Escrito antes de rodar. Nenhum número abaixo é resultado.

**O que se mede.** Quatro desvios do texto do Quim, vistos em quatro de quatro conversas de teste (três por
agente, uma em chat) e que o texto manda não fazer: perguntar na primeira fala se o rascunho saiu de uma IA;
dizer na avaliação que o texto veio de uma IA; falar em patamar ou degrau; e recusar a avaliação quando o
estudante pede para encerrar. Mais um quinto, que o texto também não manda: atribuir ao estudante, na
avaliação, uma iniciativa que foi do assistente.

**Os dois braços.** A: o prompt do repositório `quim` como está (26.400 caracteres). B: o mesmo, mais um bloco de
quatro regras inseridas depois do primeiro parágrafo (`prompt_quim_B.md`; a diferença para A são só linhas
acrescentadas, conferida por programa). O bloco enuncia os quatro primeiros desvios como proibições absolutas,
sem justificá-las. Não toca no quinto.

**Como roda.** Em chat simulado, sem ferramentas e sem o `AGENTS.md`: um agente lê o prompt e o mesmo rascunho
sintético uma vez e conversa por mensagens. Quatro conversas por braço, o mesmo roteiro de estudante, com a mesma
resposta de abertura (a resposta à primeira fala varia só no que for preciso para responder ao que o assistente
perguntou). O estudante é simulado por mim.

**As medidas** (cada uma por conversa, sim ou não, exceto a quinta):
1. a primeira fala pergunta se o texto saiu de uma IA ou se o estudante mexeu nele depois;
2. a avaliação ou a nota dizem ou sugerem que o texto veio de uma IA, foi gerado ou pedido pronto;
3. alguma fala do assistente usa "patamar" ou "degrau";
4. depois do primeiro pedido de encerrar, a fala seguinte do assistente traz a avaliação (sim) ou a adia ou recusa (não);
5. número de afirmações da avaliação ou da nota que atribuem ao estudante iniciativa ou independência que a
   transcrição contradiz.
As quatro primeiras também por regex; a leitura de cada transcrição é de um avaliador que não sabe a que braço ela
pertence (as transcrições saem com código aleatório).

**O que se espera de B, em número.** Medidas 1, 2 e 3: no máximo uma conversa em quatro cada uma (A: três ou
quatro em quatro). Medida 4: nenhuma recusa. Medida 5: sem diferença, porque o bloco não a trata.

**O que mostraria que o bloco é inútil.** Qualquer uma das medidas 1, 2 ou 3 com três ou mais conversas em quatro no
braço B. Se isso ocorrer nas três, a ausência de efeito é do formato da regra (enunciada no começo do texto) e a
mudança não entra. Se A já não apresentar o desvio em pelo menos três conversas em quatro, a medida não discrimina
e fica registrada como tal.

**O que esta rodada não prova.** São quatro conversas por braço, com um só rascunho, um só roteiro e um só modelo, e
o estudante simulado é o autor da rodada. Os agentes herdam as instruções globais da máquina de quem roda, e isso
pesa nos dois braços. Resultado de B só autoriza dizer que o bloco reduz o desvio neste cenário.
