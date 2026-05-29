# Tutorial de Uso da API Aircraft

Este tutorial ensina como subir a API, acessar a documentação Swagger e consumir os endpoints para uso em qualquer frontend.

---

## 1. Pré-requisitos

- Docker e Docker Compose instalados
- Arquivo `.env` configurado com a URL do banco PostgreSQL

---

## 2. Subindo a API com Docker Compose

No terminal, na raiz do projeto:

```bash
docker-compose up --build
```

- Isso sobe a API FastAPI na porta 8000 e o banco PostgreSQL (se estiver usando local).
- Para parar, use `CTRL+C` e depois `docker-compose down`.

---

## 3. Acessando a documentação Swagger

Com a API rodando, acesse no navegador:

```
http://localhost:8000/docs
```

- Aqui você pode testar todos os endpoints (GET, POST, DELETE etc.)
- O Swagger mostra exemplos de requisição e resposta para cada rota

---

## 4. Endpoints principais

### Companhias

- `GET /companhias` — lista todas
- `POST /companhias` — cria uma nova
- `GET /companhias/{id}` — detalhes
- `GET /companhias/iata/{codigo}` — busca por IATA
- `DELETE /companhias/{id}` — remove

### Aeronaves

- `GET /companhias/{id}/aeronaves` — lista frota
- `POST /companhias/{id}/aeronaves` — adiciona aeronave
- `GET /companhias/{id}/aeronaves/{aeronave_id}` — detalhes
- `DELETE /companhias/{id}/aeronaves/{aeronave_id}` — remove

---

## 5. Exemplo de requisição para criar companhia

```json
{
  "nome": "LATAM Airlines",
  "codigo_iata": "LA",
  "pais": "Brasil",
  "ano_fundacao": 1927
}
```

---

## 6. Observações para o frontend

- Todos os endpoints aceitam e retornam JSON
- CORS já está liberado para qualquer origem
- Use o Swagger para ver exemplos de payloads
- O banco está na nuvem, então qualquer frontend pode consumir a API de qualquer lugar

---
