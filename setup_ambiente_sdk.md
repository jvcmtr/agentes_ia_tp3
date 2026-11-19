# Guia para o setup do ambiente

## 1. Clone e acesse o repositorio:
```sh
git clone https://github.com/jvcmtr/agentes_ia_tp3.git
cd agentes_ia_tp3
```

## 2. Crie e acesse o ambiente virtual:
Crie o ambiente:
```sh
python3 -m venv venv
```

Acesse o ambiente no terminal (linux):
```sh
source venv/bin/activate
```

## 3. Instale as dependencias:
```sh
pip install -r requirements.txt
```

## 4. Inicialize as variaveis de ambiente:
Crie um arquivo nomeado `.env` na raiz do projeto e inicialize as variaveis de ambiente com os valores adequados. 

Segue aqui um exemplo de arquivo `.env`:
```txt
GEMINI_API_KEY = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```