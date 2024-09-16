import datetime
import calendar

def main():

    class Book:
             def __init__(self, title, pages, reading_time):
                self.title = title
                self.pages = pages
                self.reading_time = reading_time
    
    books = []

    while True:
        print('💫Menu💫')
        print('1. Add Book')
        print('2. Delete Book')
        print('3. Show books statistics')
        print('4. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            print()
            n_books = int(input('How many books would you like to add;'))

            for i in range(n_books):
                book_title = input(str('Title of the book that you have read:'))
                book_pages = int(input('Number of pages:'))
                reading_time = int(input('Reading time in days:')) 
                my_book = Book(book_title, book_pages, reading_time)
                books.append(my_book)
                print(f'Book {my_book.title} added!')
                
            
        elif choice == '2':
            for index, book in enumerate(books):
                print(f'{index + 1}. {book.title}')

            book_index = int(input('Enter the number of the book you want to delete:'))
            if 0 <= book_index < len(books):
                books.pop(book_index - 1)
                print('The book is removed!')

        elif choice == '3':
            def calculate_pages_daily(book_pages, reading_time):
                pages_daily = book_pages / reading_time
                return pages_daily

            def calculate_pages_yearly(pages_daily):
                current_year = datetime.datetime.now().year
                days_in_year = 366 if calendar.isleap(current_year) else 365
                pages_yearly = days_in_year * pages_daily
                return pages_yearly

            pages_daily_total = 0

            for book in books:
                print(f'Your statistics for {book.title} book:')   
                pages_daily = calculate_pages_daily(book.pages, book.reading_time)
                print(f'Currently you are reading on average {pages_daily} pages daily.')

                pages_yearly = calculate_pages_yearly(pages_daily)
                print(f'By the end of the year with this rate you will read {pages_yearly} pages.')

                pages_daily_total += pages_daily 
            
            print(f'Sum of combined average pages daily: {pages_daily_total / len(books)}')
            

        elif choice == '4':
            print('Exiting the APP.')
            break

        else:
            print('Invalid choice. Please try again.')        

main()



    


