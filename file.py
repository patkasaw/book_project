import book_file

def write_file(books):
    with open('books.txt', 'w') as file:
        raw_books = []

        for book in books:
            raw_book = ";".join([book.title, str(book.author), str(book.pages), str(book.reading_time)])
            raw_books.append(raw_book)

        file.write('\n'.join(raw_books))
    
    file.close()

def read_file():
    with open ('books.txt', 'r') as file:
        lines = file.readlines()
        books = []
        for index, line in enumerate(lines):
            raw_book = line.strip().split(';')
            if len(raw_book) == 4: # Sprawdzamy, czy mamy 4 elementy w książce
                book = book_file.Book(index + 1,  # book_id automatycznie
                                      str(raw_book[0]),  # title
                                      str(raw_book[1]),  # author
                                      int(raw_book[2]),  # pages
                                      int(raw_book[3]))  # reading_time
                books.append(book)

        return books
        