def create_bookshelf(book_list):
    clean_books_data = []

    # Looping through the docs data to extract books info
    for book in book_list:
        clean_book = {
            "book_title": book.get("title", "unknown_title"),
            "published_year": book.get("first_publish_year", "unknownDate"),
            "Author": book.get("author_name", "unknown_writer")
        }
        clean_books_data.append(clean_book)
    
    return clean_books_data