# Trabalho Prático - Teste de Software - Wordle

## Grupo
- Gabriel Pains de Oliveira Cardoso
- Lorenzo Carneiro Magalhães
- Victor de Almeida Nunes Murta

## Wordle API

API simples para o jogo Wordle/Termo em Python usando FastAPI.

### Como Executar

```bash
pip install -r requirements.txt
python run_server.py
```

Servidor: `http://localhost:8000`
Documentação: `http://localhost:8000/docs`

### Endpoints

**Criar Jogo**
```
POST /api/v1/wordle/games
```

**Fazer Tentativa**
```
POST /api/v1/wordle/games/{game_id}/guess
Body: {"word": "carro"}
```

**Ver Estado do Jogo**
```
GET /api/v1/wordle/games/{game_id}
```

### Funcionalidades

- Criação de jogos com IDs simples (1, 2, 3...)
- Validação de palavras de 5 letras
- Sistema de feedback: "correct", "present", "not present"
- Máximo 6 tentativas por jogo
- Palavra revelada quando o jogo termina

## Tecnologias

- Fastapi
- Pydantic
- Pytest
- Uvicorn
