from ORM.models import Genre
import ORM.genreRepository

def Create():
    genre = Genre()
    genre.name = input("Введите наименование жанра :>")
    try:
        ORM.genreRepository.Create(genre)
    except sqlalchemy.exc.IntegrityError as e:
        if "UNIQUE constraint failed" in e.args[0]:
            print(f"Попытка добавить повторяющееся значение {genre_name}")

def Read(genres):
    if genres == None:
        genres = ORM.genreRepository.Read()

    print(":{0:^6s}:{1:^40s}:".format("id", "наименование"))
    for g in genres:
        print(":{id:>6d}:{name:<40s}:".format(id=g.id, name=g.name))

def Update():
    genre = Genre()
    try:
        genre.id = int(input("Введите id изменяемой записи :>"))
    except ValueError:
        print("требовалось ввести числовое значение")

    if ORM.genreRepository.Read(id=genre.id) != None:
        genre.name = input(f"{genre.name} заменить на :>")
        ORM.genreRepository.Update(genre)
    else:
        print("нет записи с введённым кодом")

def Delete():
    genre = Genre()
    try:
        genre.id = int(input("Введите id удаляемой записи :>"))
    except ValueError:
        print("требовалось ввести числовое значение")

    if ORM.genreRepository.Read(id=genre.id) != None:
        ORM.genreRepository.Delete(genre)
    else:
        print("нет записи с введённым кодом")