"""Simple Library API simulation — plain Python only (no web server)."""

from __future__ import annotations

import asyncio

# In-memory list of books (like a tiny database in RAM)
BOOKS: list[dict[str, int | str | bool]] = [
    {"id": 1, "title": "Intro to Data Structures", "author": "Maraima Barrie", "available": True},
    {"id": 2, "title": "Short Stories", "author": "Amie", "available": True},
    {"id": 3, "title": "Math for Beginners", "author": "Sulaman", "available": True},
    {"id": 4, "title": "Computer Basics", "author": "Zakaria", "available": True},
    {"id": 5, "title": "Python Workshop", "author": "Kamara", "available": True},
]


async def get_books() -> list[dict[str, int | str | bool]]:
    """Simulates GET /books — returns the full catalog."""
    return list(BOOKS)


async def borrow_book(user_id: int, book_id: int) -> dict[str, object]:
    """Simulates POST /borrow — checks the book, then marks it unavailable if possible."""
    # Pretend we are waiting on a network or database
    await asyncio.sleep(1)

    for book in BOOKS:
        if book["id"] != book_id:
            continue
        if not book["available"]:
            return {
                "ok": False,
                "message": "Error: book is not available (already borrowed).",
                "user_id": user_id,
                "book_id": book_id,
            }
        book["available"] = False
        return {
            "ok": True,
            "message": "Borrowed successfully.",
            "user_id": user_id,
            "book_id": book_id,
            "title": book["title"],
        }

    return {
        "ok": False,
        "message": "Error: book does not exist.",
        "user_id": user_id,
        "book_id": book_id,
    }


async def main() -> None:
    """Run a tiny demo: list books, borrow one, try to borrow again, show final list."""
    print("--- GET /books -> get_books() ---")
    books = await get_books()
    for b in books:
        print(b)

    print("\n--- POST /borrow -> borrow_book(user_id=1, book_id=1) ---")
    first = await borrow_book(1, 1)
    print(first)

    print("\n--- POST /borrow again (same book, should fail) ---")
    second = await borrow_book(2, 1)
    print(second)

    print("\n--- Catalog after borrows ---")
    for b in await get_books():
        print(b)


if __name__ == "__main__":
    asyncio.run(main())
