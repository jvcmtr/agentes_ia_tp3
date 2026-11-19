import os
import sys
from dotenv import load_dotenv
from google import genai
from verificar_ambiente import verificar

MODEL = "gemini-3.5-flash-lite"
INSTRUCOES_CANCELAMENTO = """
Você é o assistente da equipe de retenção da NeoStream, uma plataforma de streaming. 
Você tem o papel de auxiliar os analistas e demais funcionarios a responder perguntas gerais 
sobre a política de cancelamento da empresa. Seja sempre breve e objetivo em suas respostas.
"""

class GeminiAgent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

    def question(self, q):
        return self.instructions + " ---- PERGUNTA DO FUNCIONARIO: " + q

def criar_agente(name = "AgenteCancelamento" ):
    return GeminiAgent(name , INSTRUCOES_CANCELAMENTO, MODEL)


def executar_pergunta(agent, pergunta):
    print("_"*40)
    print(f"PERGUNTA: \"{pergunta}\" ")
    
    client = genai.Client()
    interaction = client.interactions.create(
        model = agent.model,
        input= agent.question(pergunta),
        # config=types.GenerateContentConfig(
        #     #  
        #     thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.MINIMAL),
        #     max_output_tokens=120,
        # ),
    )
    resp = interaction.output_text
    print(f"RESPOSTA: \"{resp}\" ")
    return resp


def main():
    verificar()

    agente = criar_agente()

    perguntas = [
        "Um assinante do plano anual cancela o plano 30 dias antes do final do plano, ele deve receber um reembolso?",
        "Se um assinante do plano premium com mais de 2 anos de uso da plataforma enuncia que deseja cancelar o seu plano, qual a maior margem de desconto que posso fornescer para retenção do cliente.",
    ]
    resultados = []

    for p in perguntas:
        resultados.append( {"pergunta": p, "resposta": executar_pergunta(agente, p)} )

    print("\n\n---\n Execução finalizada. Output:")
    print(resultados)


if __name__ == "__main__":
    main()