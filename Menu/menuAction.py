import sys
import sqlalchemy.exc

import Views.genreView
import Views.bookView

def Choise(action):
    match action:
        case "books.add":
            Views.bookView.Create()
        case "books.show":
            print("!!!")
        case "genres.add":
            Views.genreView.Create()
        case "genres.show":
            Views.genreView.Read(None)
        case "genres.upd":
            Views.genreView.Update()
        case "genres.del":
            Views.genreView.Delete()
