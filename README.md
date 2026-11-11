# Oficina Pedagógica

Assistentes conversacionais para exercícios de escrita na graduação em Direito.
Desenvolvidos por Alexandre Araújo Costa, Faculdade de Direito da UnB, com
assistência do Claude Opus em Claude Code.

Cada assistente acompanha o estudante na revisão de um texto que ele mesmo
escreveu. Pergunta em vez de corrigir, não redige trecho nenhum no lugar do
estudante e, ao fim, escreve uma avaliação curta, sem nota, que o estudante
entrega junto com uma nota sobre a conversa. A oficina nasceu na disciplina
Introdução ao Direito 1 e é a quarta das Oficinas Acadêmicas, ao lado das
oficinas de [Projetos](https://github.com/AlexandreAraujoCosta/Oficina_de_Projetos),
de [Orientação](https://github.com/AlexandreAraujoCosta/Oficina_de_Orientacao) e de
[Formatação](https://github.com/AlexandreAraujoCosta/Oficina_de_Formatacao).

Este repositório traz **a maquinaria, e nunca o material**: prompts, páginas e
guias de uso, sem texto de estudante, sem conversa de aula e sem avaliação de
pessoa nomeada.

## Os assistentes

**Quim.** A reescrita contemporânea de *Teoria do Medalhão*, de Machado de Assis.
A conversa procura o que o texto faz com a ironia do original e o que ele
desloca dela, e usa perguntas que ligam mais de um ponto do rascunho quando o
texto já chega elaborado. Repositório: [quim](https://github.com/AlexandreAraujoCosta/quim).

**Ana.** O voto de desempate no Caso dos Exploradores de Cavernas, de Lon Fuller.
A conversa é maiêutica e inclui uma rodada de objeção: a melhor razão do lado
contrário ao voto. Repositório: [ana](https://github.com/AlexandreAraujoCosta/ana).

**Miguel.** As fontes do direito, pela posição do juiz. O estudante decide um caso
penal e o assistente examina a fundamentação, sem corrigir a decisão, até o ponto
em que a norma que decidiu o caso foi criada pelo próprio juiz. Em
desenvolvimento.

## Como se usa

Os três são **prompts portáteis**: um texto que se cola como primeira mensagem em
qualquer assistente de IA gratuito, sem instalar nada. O Quim e a Ana foram
testados com o Claude Sonnet, o modelo das contas gratuitas. Os modos rápidos dão
resultado ruim nesta atividade: o assistente conversa de forma superficial e pode
inventar o que não aconteceu na conversa. Leia a avaliação antes de colá-la como
entrega, e peça a correção se ela atribuir ao estudante algo que ele não disse.

## Por um agente

Os mesmos três assistentes rodam num agente (Claude Code, ou o VS Code com uma
extensão em modo agente). O agente clona esta oficina na pasta do estudante, lê o
`AGENTS.md` e o texto do assistente em `assistentes/`, e conduz a conversa na
própria sessão. O pedido que se cola no agente está na
[página da oficina](https://claude.ai/artifact/JagCaPZjYaNJDF4PMAkwgL), com um
clique para copiar.

O que muda em relação ao chat: o rascunho é um arquivo da pasta, e não texto
colado; o agente mantém um registro da conversa, rodada a rodada, de onde sai a
nota sobre a conversa, em vez de reconstruí-la de memória; e a avaliação com a
nota saem num arquivo de entrega. Os textos em `assistentes/` são cópias dos
prompts portáteis, geradas por `scripts/montar_assistentes.py`: a fonte de cada
um é o repositório do assistente, ou o artifact, no caso do Miguel.

**Este formato foi testado uma vez**, com um agente e um estudante simulado (uma
conversa de três rodadas sobre o Quim). Não houve conversa de aula nem medição. O
teste achou duas falhas, uma citação do rascunho digitada com uma palavra trocada e
uma observação do agente atribuída ao estudante na avaliação, e o `AGENTS.md` foi
ajustado para elas sem nova medição. O registro da conversa é uma hipótese sobre
como tornar a nota mais fiel.

O pedido usa só o git e arquivos da pasta e não depende do Windows: no Linux muda apenas a instalação do agente.

## Autoria e estado

Concepção, critérios e prompts: Alexandre Araújo Costa, Universidade de Brasília.
Abordagem experimental, em fase de testes. Quem usar os assistentes pode relatar o
resultado por [este formulário](https://forms.gle/BHhKZSQiRq1JUgsE8), pensado para
quem não está matriculado na disciplina.
