# Exercicio 1

### Contexto

O modelo de churn que você entregou no TP2 está pronto, mas seu tech lead na NeoStream quer que a próxima entrega vá além de um script que só retorna 0 ou 1: ele quer um componente capaz de receber uma pergunta em linguagem natural do time de retenção, decidir por conta própria quais informações precisa reunir e produzir uma resposta fundamentada. Antes de escrever qualquer código, ele pediu que você documente, em termos de arquitetura, o que diferencia esse componente de um script tradicional de previsão.

### Tarefa
1. Descreva o ciclo perceber-raciocinar-agir aplicado ao cenário do time de retenção: o que o componente perceberia, sobre o que raciocinaria e que ação tomaria.
2. Compare esse ciclo com o fluxo linear de um script tradicional (entrada fixa → função → saída fixa), destacando pelo menos duas diferenças arquiteturais concretas.
3. Registre a análise em arquitetura_perceber_raciocinar_agir.md.

---

### Item 1.1
No cenario descrito, o cliclo perceber-pensar-agir seria aplicado na seguinte sequencia:
- Perceber: A interface recebe a pergunta do time de retenção em forma de linguagem natural, não estruturada.
- Pensar: O modelo identifica a intenção da pergunta, planeja a coleta de informações nescessarias para a resposta e verifica se as fontes encontradas são suficientes para gerar uma resposta.
- Agir: O modelo busca as informações nescessarias para a geração da resposta atravéz de APIs, queries ou outras integrações. Apartir destes dados, o modelo gera uma resposta para a pergunta original.

### Item 1.2
O ciclo perceber-pensar-agir difere-se do script tradicional no sentido em que funciona como orquestrador do processo e não como uma função deterministica. Em termos arquiteturais, o script não possui memoria e cada requisição é tratada de forma independente, enquanto isso, o agente é adaptavel e é capaz de reunir dados sob demanda. 