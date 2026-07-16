from api import fetchLibraryData
from users import create_bookshelf

raw_data = fetchLibraryData()
# print(type(raw_data))

# the raw data contains "docs" list, within this there are books in the form of dictionary
# this returns a list of dictionaries
book_list = raw_data.get("docs", [])

# clean books data 
clean_book_list = create_bookshelf(book_list)

# printing data
for i, book in enumerate(clean_book_list[:10]):
    print(f"{i}. '{book['book_title']}' by {book['Author']} published on {book['published_year']}")

