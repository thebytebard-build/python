# List to store transactions
transactions = []

# Import functions from other modules using relative import
from .books import book_exists
from .members import member_exists

def borrow_book(member_id, book_id):
    if not member_exists(member_id):
        print("Member does not exist!")
        return
    if not book_exists(book_id):
        print("Book does not exist!")
        return
    
    transactions.append((member_id, book_id))
    print(f"Member {member_id} borrowed book {book_id}")

def show_transactions():
    for t in transactions:
        print(f"Member {t[0]} borrowed book {t[1]}")
