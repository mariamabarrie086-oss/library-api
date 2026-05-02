"""Library Management API — single-file FastAPI app. Run: uvicorn main:app --reload"""

from __future__ import annotations

import asyncio

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# In-memory catalog (id -> book fields)
books: dict[int, dict[str, str | bool]] = {
    1: {"title": "Introduction to Algorithms", "author": "Cormen et al.", "available": True},
    2: {"title": "Clean Architecture", "author": "Robert C. Martin", "available": True},
    3: {"title": "Python Crash Course", "author": "Eric Matthes", "available": True},
}

app = FastAPI(title="Library API", version="1.0.0")


class BorrowReturnBody(BaseModel):
    user_id: int = Field(..., ge=1)
    book_id: int = Field(..., ge=1)


@app.get("/books")
async def get_books() -> dict[str, object]:
    listed = [{"id": bid, **data} for bid, data in books.items()]
    return {"message": "OK", "data": {"books": listed}}


@app.post("/borrow")
async def borrow(body: BorrowReturnBody) -> JSONResponse:
    await asyncio.sleep(1)
    book = books.get(body.book_id)
    if book is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Book not found.", "data": None},
        )
    if not book["available"]:
        return JSONResponse(
            status_code=400,
            content={"message": "Book is not available.", "data": {"book_id": body.book_id}},
        )
    book["available"] = False
    return JSONResponse(
        content={
            "message": "Borrowed successfully.",
            "data": {
                "user_id": body.user_id,
                "book_id": body.book_id,
                "title": book["title"],
            },
        }
    )


@app.post("/return")
async def return_book(body: BorrowReturnBody) -> JSONResponse:
    await asyncio.sleep(1)
    book = books.get(body.book_id)
    if book is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Book not found.", "data": None},
        )
    book["available"] = True
    return JSONResponse(
        content={
            "message": "Returned successfully.",
            "data": {"user_id": body.user_id, "book_id": body.book_id},
        }
    )
