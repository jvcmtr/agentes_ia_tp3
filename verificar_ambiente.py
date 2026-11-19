import os
import sys
from dotenv import load_dotenv

ENV = load_dotenv()

def arquivo_env_carregado() -> bool:
    return bool(ENV)


def chave_api_presente() -> bool:
    chave = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    return bool(chave and chave.strip())


def sdk_google_genai_disponivel() -> bool:
    try:
        from google import genai
        return True
    except ImportError:
        return False



VERIFICACOES = [
    {
        "nome": "Arquivo .env existe",
        "erro": "Arquivo .env não encontrado. Gere um arquivo '.env' na raiz do projeto.",
        "func": arquivo_env_carregado,
    },
    {
        "nome": "Variável GEMINI_API_KEY (ou GOOGLE_API_KEY) definida",
        "erro": "Chave de API não encontrada no ambiente. Defina GEMINI_API_KEY no seu arquivo .env.",
        "func": chave_api_presente,
    },
    {
        "nome": "Biblioteca google-genai instalada",
        "erro": "Biblioteca google-genai não encontrada. Instale com: pip install google-genai",
        "func": sdk_google_genai_disponivel,
    }
]

def verificar():
    print("_"*40)
    print("Iniciando verificação de ambiente:")

    for v in VERIFICACOES:
        print(f"[+] Verificando {v['nome']}")
        if v['func']():
            print("[+] OK")
        else: 
            print(f"[-] {v['erro']}")


if __name__ == "__main__":
    verificar()