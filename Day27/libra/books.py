# List of books (dictionary: book_id -> title)
books = {
    1: "Python Programming",
    2: "Data Structures",
    3: "Algorithms"
}

# Function to show all books
def list_books():
    for book_id, title in books.items():
        print(f"{book_id}: {title}")

# Function to check if a book exists
def book_exists(book_id):
    return book_id in books

