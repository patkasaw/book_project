import book_file

def write_file(books):
    with open('books.txt', 'w') as file:
        raw_books = []

        for book in books:
            raw_book = ";".join([book.title, str(book.pages), str(book.reading_time)])
            raw_books.append(raw_book)

        file.write('\n'.join(raw_books))
    
    file.close()

def read_file():
    with open ('books.txt', 'r') as file:
        lines = file.readlines()
        books = []
        for line in lines:
            raw_book = line.split(';')
            book = book_file.Book(raw_book[0], int(raw_book[1]), int(raw_book[2]))
            books.append(book)

        return books
        