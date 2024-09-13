import datetime
import calendar

book_title = input(str('Title of the book that you have read:'))
book_pages = int(input('Number of pages:'))
reading_time = int(input('Reading time in days:'))

class Book:
    def __init__(self, book_title, book_pages, reading_time):
        self.book_title = book_title
        self.book_pages = book_pages
        self.reading_time = reading_time


def calculate_pages_daily(book_pages, reading_time):
     pages_daily = book_pages / reading_time
     return pages_daily

def calculate_pages_yearly(pages_daily):
    current_year = datetime.datetime.now().year
    days_in_year = 366 if calendar.isleap(current_year) else 365
    pages_yearly = days_in_year * pages_daily
    return pages_yearly

my_book = Book(book_title, book_pages, reading_time)

pages_daily = calculate_pages_daily(my_book.book_pages, my_book.reading_time)

pages_yearly = calculate_pages_yearly(pages_daily)



print(f'Your statistics for {book_title} book:')   


print(f'Currently you are reading on average {pages_daily} pages daily.')


print(f'By the end of the year with this rate you will read {pages_yearly} pages.')

