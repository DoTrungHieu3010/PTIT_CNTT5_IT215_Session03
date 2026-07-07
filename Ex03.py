from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": False
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": True
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": False
    }
]

@app.get("/health")
def check_api():
    return {"message": "Library API is running"}


@app.get("/books")
def get_all_books():
    book_list = []
    for i in books:
        book_list.append(i)
    return book_list

@app.get("/books/available")
def get_available_books():
    available_books = [book for book in books if book["is_available"] == True]
    return available_books

@app.get("/books/borrowed")
def get_borrowed_books():
    borrowed_book = [book for book in books if book["is_available"] == False]
    return borrowed_book

@app.get("/books/statistics")
def get_statistics():
    total_books = 0
    available_books = 0
    borrowed_books = 0
    for book in books:
        if book["is_available"] == True:
            total_books += 1
            available_books += 1
        if book["is_available"] == False:
            total_books += 1
            borrowed_books += 1
            
    return {"total_books": total_books,"available_books": available_books,"borrowed_books": borrowed_books}

@app.get("/books/categories")
def get_categories():
    categories = set(book["category"] for book in books)
    return {"category": list(categories)}

@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {"message": "No books available"}
    latest_book = books[0]
    for book in books:
        if book["year"] > latest_book["year"]:
            latest_book = book
    return latest_book
            