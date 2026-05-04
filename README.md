# Simple Library API Simulation

This project is a **Python simulation of API-style behavior** using plain functions. There is **no web server** and **no frameworks**—only the standard library (`asyncio`). It helps you practice how `GET` and `POST` style actions can be modeled as async functions.

## Simulated endpoints

| HTTP idea | Python function |
|-----------|-----------------|
| `GET /books` | `get_books()` |
| `POST /borrow` | `borrow_book(user_id, book_id)` |

- `GET /books` -> `get_books()`
- `POST /borrow` -> `borrow_book(user_id, book_id)`

## How to run

```bash
python main.py
```

You should see the catalog printed, then the result of a borrow, a failed second borrow on the same book, and the updated catalog.
