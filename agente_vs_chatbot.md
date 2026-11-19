# Exercício 2

### Contexto

Na reunião de planejamento, um gerente de produto perguntou se o componente descrito no Exercício 1 é "só um chatbot com acesso ao modelo de churn". Seu tech lead pediu que você prepare uma resposta técnica clara para essa pergunta, já que a diferença impacta diretamente o escopo do projeto e as expectativas do time de produto sobre o que o componente pode fazer de forma autônoma.

### Tarefa
1. Liste pelo menos três características que diferenciam um agente de IA de um chatbot tradicional e de um software convencional baseado em regras.

2. Aplique essas características ao cenário da NeoStream, explicando por que o componente de análise de churn deve ser projetado como agente e não como chatbot.

3. Registre a comparação em agente_vs_chatbot.md, incluindo pelo menos um caso de uso em que um chatbot simples seria suficiente e não justificaria a complexidade de um agente.

---

### Item 2.1

Um agente de IA diferencia-se de um chat-bot principalmente pelas seguintes caracteristicas:
- Um agente de IA é independente na sua escolha de ferramentas e fluxo de trabalho, sendo capaz de gerar as estrategias de coleta e consulta de  dados nescessarios para a resposta, enquanto um chat-bot sempre está limitado aos dados que lhe foram dados.

- Um agente de IA é capaz de adaptar-se em tempo real a erros de integração e falhas de conexão, podendo elaborar extrategias alternativas para a obtenção das informações, enquanto um chatbot é limitado pelos dados que lhe foram fornescidos.

- Um agente de IA é capaz de interpretar problemas complexos, decompondo problemas em subproblemas e componentes menores, enquanto um chatbot não possui tal flexibilidade na interpretação do comando.

### Item 2.2
A utilização de um agente é ideal no cenario da identificação de churn já que o objetivo do sistema é ser capaz de auxiliar o time de retenção em uma ampla gama de atividades e cenários. 

### Item 2.3
Um caso de uso que poderia ser satisfeito com um chatbot simples no contexto da empresa seria a realização de consultas/calculos apontados a um cliente especifico. 