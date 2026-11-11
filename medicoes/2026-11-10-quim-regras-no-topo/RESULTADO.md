# Rodada de medição do prompt do Quim: resultado (10/11/2026)

O plano, escrito antes de rodar, está em `PLANO-MEDICAO.md`. As transcrições (conversas sintéticas, sem
texto de estudante) estão em `transcricoes/`, com código aleatório; a chave dos códigos está em
`CHAVE_CODIGOS.txt`.

## O que rodou

Oito conversas em chat simulado, sem ferramentas e sem o `AGENTS.md`, com o mesmo rascunho sintético e o mesmo
roteiro de estudante: quatro com o prompt do repositório `quim` (braço A) e quatro com o mesmo prompt mais o bloco
de quatro regras do começo (braço B, `montar_B.py`; a diferença é só de linhas acrescentadas, conferida por
programa). As medidas 1 a 4 foram contadas por expressão regular, com controle positivo e negativo que o
programa tem de acertar, e conferidas por um avaliador que não sabia a que braço cada transcrição pertencia. Os
dois métodos concordaram em todas as 32 respostas.

## Resultado

| Medida | Braço A | Braço B |
|---|---|---|
| 1. A primeira fala pergunta se o texto saiu de uma IA | 4 de 4 | 0 de 4 |
| 2. A avaliação diz ou sugere que o texto veio de uma IA | 4 de 4 | 0 de 4 |
| 3. Alguma fala nomeia patamar ou degrau | 4 de 4 | 0 de 4 |
| 4. Depois do pedido de encerrar, a fala seguinte traz a avaliação | 4 de 4 | 4 de 4 |
| 5. Atribuições de iniciativa contraditas pela transcrição (conversas com ao menos uma) | 3 de 4 (3 afirmações) | 1 de 4 (1 afirmação) |

**Contra os critérios escritos antes.** As medidas 1, 2 e 3 ficaram em 0 de 4 no braço B, abaixo do limite de
uma em quatro, e em 4 de 4 no braço A, de modo que discriminam. Nenhuma ficou em três ou mais no braço B, que era
o critério de fracasso do bloco. A medida 4 não discrimina: o braço A não recusou a avaliação em nenhuma conversa,
embora a recusa tenha aparecido uma vez nas conversas por agente anteriores, e por isso ela não diz nada sobre o
bloco. A medida 5 era esperada sem diferença, e o resultado foi 3 contra 1. Com quatro conversas por braço isso
não permite afirmar efeito (teste exato de Fisher bilateral, p = 0,49), e fica registrado como não explicado.

## O que o resultado autoriza dizer

Neste cenário (um rascunho, um roteiro, um modelo, quatro conversas por braço), colocar no começo do prompt as quatro
proibições eliminou a pergunta sobre a origem do texto, a menção à IA na avaliação e o vocabulário de patamar.

## O que ele não autoriza

- **A medida 2 não é independente da 1.** No braço A o estudante simulado responde "Saiu de uma IA sim" à
  pergunta do assistente, e a avaliação repete o que ele disse. No braço B ele nunca diz isso. O efeito sobre a
  medida 2 pode vir só de a pergunta não ter sido feita. A medida 3 não tem esse problema.
- **O bloco não toca na atribuição de iniciativa**, e a falha continua nos dois braços: quatro afirmações contraditas
  em oito conversas, todas do mesmo tipo (dizer que o estudante achou "sozinho" que a frase do agradável explica
  demais, quando o assistente a apontou na primeira fala e o estudante respondeu "eu também acho"). O avaliador achou
  o mesmo erro em duas falas intermediárias, uma em cada braço, fora da avaliação e da nota.
- **Outros defeitos achados pelo avaliador, sem contagem própria:** em uma conversa do braço A a avaliação diz que o
  texto está "bem abaixo da extensão pedida", sem que a conversa fale de extensão, e se contradiz sobre os detalhes
  que "não se explicam"; em uma do braço B a contagem de mensagens do estudante não bate com o que a transcrição mostra.
- Os agentes herdam as instruções globais da máquina de quem roda, o estudante é simulado por quem escreveu o
  plano, e o rascunho é um só. Quatro conversas por braço não medem frequência.

## Decisão

O plano disse que o bloco entra se as medidas 1, 2 e 3 ficassem em no máximo uma de quatro no braço B. Passou. Aplicar
no prompt publicado (repositório `quim` e artifact do Quim) é decisão do autor, e a mudança entra carimbada como
medida em 10/11/2026 sobre quatro conversas por braço. A atribuição de iniciativa segue sem tratamento no prompt.
