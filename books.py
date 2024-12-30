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
        print('2. Delete Book')
        print('3. Show books statistics')
        print('4. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            add_book()
            
        elif choice == '2':
            delete_book()

        elif choice == '3':
            show_statistics()

        elif choice == '4':
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

        my_book = book_file.Book(book_title, book_pages, reading_time)
        books.append(my_book)

        file.write_file(books)

        print(f'Book {my_book.title} added!')
    
def delete_book():
    if books == []:
        print('The list is empty. Yo cannot delete anything.')
        return
    
    for index, book in enumerate(books):
        print(f'{index + 1}. {book.title}')
    
    try:
        book_index = int(input('Enter the number of the book you want to delete:'))
    except ValueError:
        print('Podana wartosć nie jest liczbą. Spróbój ponownie.')
        return

    if 0 < book_index <= len(books):
        books.pop(book_index - 1)
        print('The book is removed!')
    elif len(book) < book_index:
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



    


