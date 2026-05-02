# Library API (single-file)

Minimal FastAPI library demo for coursework.

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
