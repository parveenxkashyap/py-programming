class Book:
    def __init__(self, title, author, isbn):  # Use double underscores for '__init__'
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            isbn = input("Enter the ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            title = input("Enter the book title to search: ")
            found_book = library.search_book(title)
            if found_book:
                print(f"Book found - Title: {found_book.title}, Author: {found_book.author}, ISBN: {found_book.isbn}")
            else:
                print("Book not found.")

        elif choice == '3':
            print("Exiting the library management system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
