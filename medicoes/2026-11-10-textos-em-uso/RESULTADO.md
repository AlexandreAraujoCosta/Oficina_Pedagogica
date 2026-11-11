# Medição do texto em uso do Quim e da Ana: resultado (10/11/2026)

O plano, escrito antes de rodar, está em `PLANO-MEDICAO.md`. Os textos medidos são os das páginas em uso
(`assistentes/quim.md`, 35.918 caracteres, e `assistentes/ana.md`, 53.857). As transcrições, com código aleatório, estão
em `transcricoes/`, e a chave em `CHAVE_CODIGOS.txt`.

## O que rodou

Oito conversas em chat simulado, sem ferramentas e sem `AGENTS.md`: quatro com o Quim (rascunho sintético sobre
"Teoria do Medalhão") e quatro com a Ana (voto sintético sobre o caso dos exploradores de cavernas), o mesmo roteiro de
estudante em cada assistente. As medidas 1 a 4 foram contadas por expressão regular, com controle positivo e negativo, e
todas as seis por um leitor que não sabia a que assistente cada transcrição pertencia. As respostas dos dois métodos
coincidiram nas medidas 1 a 4.

## Resultado

| Medida | Quim | Ana |
|---|---|---|
| 1. A primeira fala pergunta se o texto saiu de uma IA | 0 de 4 | 0 de 4 |
| 2. A avaliação diz ou sugere que o texto veio de uma IA | 0 de 4 | 0 de 4 |
| 3. Alguma fala nomeia patamar, degrau ou nível | 0 de 4 | 0 de 4 |
| 4. Depois do pedido de encerrar, a fala seguinte traz a avaliação | 4 de 4 | 4 de 4 |
| 5. Atribuições de iniciativa contraditas pela transcrição | 0 de 4 | 0 de 4 |
| 6. Aspas na avaliação reproduzindo palavras do estudante | 0 de 4 | 0 de 4 |

Das 19 afirmações de iniciativa examinadas pelo leitor, 18 se sustentam e uma é indeterminada. Todas as aspas que a
contagem por regex achou nas avaliações do Quim reproduzem o rascunho comentado, e não palavras do estudante; a contagem
por regex, que não distingue uma coisa da outra, sozinha teria dado um falso positivo.

## Contra o plano

As medidas 1, 2 e 3 ficaram em 0 de 4 nos dois assistentes. O plano dizia que o texto em uso não faria o que diz se
alguma delas chegasse a três de quatro: não chegou, e o bloco de regras testado em 10/11 sobre a cópia antiga não tem
motivo para ser aplicado ao texto em uso. A medida 5 era esperada em ao menos duas de quatro por assistente, e deu zero.
A hipótese de que a falha de atribuição se repetiria no texto em uso caiu neste cenário. Nas 14 conversas anteriores,
todas sobre as cópias antigas, a falha tinha aparecido em 9 (contando uma avaliação em que só metade da atribuição estava errada).

## O que o resultado não autoriza dizer

- O cenário da Ana é mais favorável à medida 5 do que o do Quim. Na Ana, o assistente pede primeiro que o estudante diga
  o que decidiu, e o estudante traz a dúvida sobre a clemência antes de o assistente apontar qualquer coisa: a atribuição
  de iniciativa a ele é correta por construção. No Quim, o assistente aponta antes o ponto que o estudante depois repete, e
  nesse cenário a falha não apareceu, mas uma avaliação (C04) credita ao estudante "ver" o que o assistente formulou
  primeiro, sem usar "sozinho". O leitor a registrou à parte, fora da medida 5.
- Quatro conversas por assistente, um rascunho por assistente, um só modelo, estudante simulado por quem escreveu o plano,
  agentes que herdam as instruções globais da máquina de quem roda.

## Outros defeitos achados pelo leitor, sem contagem prevista no plano

Aparecem em cinco das oito conversas, e são pequenos, todos de coerência interna da avaliação ou da nota:
- duas avaliações da Ana dizem que o estudante "respondeu às duas perguntas", e a nota da mesma avaliação registra que uma
  ficou sem resposta;
- a avaliação de uma conversa do Quim diz que o parágrafo final foi apontado na abertura, e a abertura não o apontou; em
  outra diz "sem pedir a linha escrita" quando o assistente a tinha pedido;
- duas notas da Ana mencionam uma pergunta "que não chegou a ser feita", que o estudante nunca viu;
- uma avaliação do Quim está inteira em terceira pessoa ("o estudante imaginou"), num texto que o estudante vai colar;
- "insisti duas vezes no mesmo ponto" foi contado de modos diferentes em conversas com o mesmo desenho.
