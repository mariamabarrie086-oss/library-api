# library-api

A simple FastAPI-based Library Management API with async endpoints for borrowing and returning books.

Minimal single-file demo (`main.py`) for coursework.

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to try the API.

## Endpoints

- `GET /books` — list all books
- `POST /borrow` — JSON body: `user_id`, `book_id`
- `POST /return` — JSON body: `user_id`, `book_id`

Responses use `{"message": "...", "data": ...}`.
