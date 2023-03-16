from ORM.models import Book, Author
import ORM.bookRepository
import ORM.authorRepository

def Create():
    book = ORM.models.Book()
    print("Введите")
    book.title = input("наименование книги :>")
    while True:
        try:
            i = int(input("год издания :>"))
        except ValueError:
            print("ожидается ввод числового значения")
        else:
            break
    book.year_of_issue = i


