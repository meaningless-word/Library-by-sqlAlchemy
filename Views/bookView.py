import Views.genreView
from ORM.models import Book, Author
import ORM.bookRepository
import ORM.authorRepository
from ORM.genreRepository import Read as genreRead

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
    while True:
        s = input("введите часть наименования жанра чтобы определить круг поиска:>")
        genres = genreRead(sub=s)
        if len(genres) == 1:
            book.genre = genres[0]
            print(f"жанр {genres[0].name} определен однозначно")
            break
        elif len(genres) > 1:
            # в выборку попало несколько записей - вывести для дальнейшего уточнения
            Views.genreView.Read(genres)
            break

