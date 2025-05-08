import datetime
import calendar
import file
import book_file


books = file.read_file()

def menu():
    is_running = True

    while is_running:
        print()
        print('💫Menu💫')
        print('1. Add Book')
        print('2. Show all books')
        print('3. Update book')
        print('4. Delete Book')
        print('5. Show books statistics')
        print('6. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            add_book()

        elif choice == '2':
            show_books()
            
        elif choice == '3':
            update_book()

        elif choice == '4':
            delete_book()

        elif choice == '5':
            show_statistics()

        elif choice == '6':
            is_running = exit_app()
        

        else:
            print('Invalid choice. Please try again.')        

def add_book():
    print()
    try:
        n_books = int(input('How many books would you like to add:'))
    except ValueError:
        print('Given value is not a number. Please try again.')
        return

    for i in range(n_books):
        book_title = input(str('Title of the book that you have read:'))
        book_author = input(str('Author of the book that you have read:'))
        while True:
            try:
                book_pages = int(input('Number of pages:'))
                break
            except ValueError:
                print('Given value is not a number. Please try again.')

        while True:
            try:
                reading_time = int(input('Reading time in days:'))
                break
            except ValueError:
                print('Given value is not a number. Please try again.')

        my_book = book_file.Book(book_title, book_author, book_pages, reading_time)
        books.append(my_book)

        file.write_file(books)

        print(f'Book {my_book.title} added!')

def show_books():
    if books == []:
        print('The list is empty.')
        return
    
    for index, book in enumerate(books):
        print(f'{index + 1}. {book.title}')

def update_book():
    show_books()

    try:
        book_index = int(input('Enter the number of the book you want to update:'))
    except ValueError:
        print('Podana wartosć nie jest liczbą. Spróbój ponownie.')
        return
    
    if book_index <= 0 or len(books) < book_index:
        print('This number don''t exist.')
        return
    elif book_index == 0:
        print('No books to update.') 
        return
    
    if 0 < book_index <= len(books):
        book_to_update = books[book_index - 1]
        print(f'1.{book_to_update.title}')
        print(f'2.{book_to_update.author}')
        print(f'3.{book_to_update.pages}')
        print(f'4.{book_to_update.reading_time}')
        update_choice = int(input('Enter your choice:'))
        if update_choice == 1:
            new_book_title = input(str('New book title:'))
            book_to_update.title = new_book_title
            print('Title has been changed')

        if update_choice == 2:
            new_book_author = input(str('New book author:'))
            book_to_update.author = new_book_author
            print('Title has been changed')

        if update_choice == 3:
            try:
                new_book_pages = int(input('New book pages:'))
            except ValueError:
                print('Given value is not a number. Please try again.')
                return
            book_to_update.pages = new_book_pages
            print('Pages has been updated')
        
        if update_choice == 4:
            try:
                new_book_reading_time = int(input('New book reading time:'))
            except ValueError:
                print('Given value is not a number. Please try again.')
                return
            book_to_update.reading_time = new_book_reading_time
            print('Reading time has been updated')

    file.write_file(books)

def delete_book():
    show_books()
    
    try:
        book_index = int(input('Enter the number of the book you want to delete:'))
    except ValueError:
        print('Podana wartosć nie jest liczbą. Spróbój ponownie.')
        return

    if 0 < book_index <= len(books):
        books.pop(book_index - 1)
        print('The book is removed!')
    elif book_index <= 0 or len(books) < book_index:
            print('This number don''t exist.')
    else:
        if book_index == 0:
            print('No books to delete.') 

    file.write_file(books)
    

def show_statistics():
    def calculate_pages_daily(book_pages, reading_time):
        pages_daily = book_pages / reading_time
        return pages_daily

    def calculate_pages_yearly(pages_daily):
        current_year = datetime.datetime.now().year
        days_in_year = 366 if calendar.isleap(current_year) else 365
        pages_yearly = days_in_year * pages_daily
        return pages_yearly

    pages_daily_total = 0

    if len(books) <= 0:
        print('No books to show statistics')
        return

    for book in books:
        print(f'Your statistics for {book.title} book:') 
        
        pages_daily = calculate_pages_daily(book.pages, book.reading_time)
        print(f'Currently you are reading on average {pages_daily} pages daily.')
        
        pages_yearly = calculate_pages_yearly(pages_daily)
        print(f'By the end of the year with this rate you will read {pages_yearly} pages.')
        
        pages_daily_total += pages_daily 
        print(f'Sum of combined average pages daily: {pages_daily_total / len(books)}')
        
def exit_app():
    print('Exiting the APP.')
    return False
                             
menu()



    


