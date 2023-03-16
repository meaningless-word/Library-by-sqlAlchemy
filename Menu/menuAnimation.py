import Menu.menuAction as Do

def menuDraw(m, Title=""):
    itemLength = 30
    while True:
        if len(Title) > 0: print(Title)
        for k, v in m.items():
            print("{0:s}{1:d}".format(v[0] + (itemLength - len(v[0])) * ".", k))
        print("{0:s}{1:d}".format(("Выход" + itemLength * ".")[:itemLength], 0))

        try:
            selected = int(input(":>"))
        except:
            selected = -1
            print("ожидается цифра")

        if selected in m:
            if len(m[selected]) == 3:
                Do.Choise(m[selected][2])
            elif len(m[selected]) == 2:
                menuDraw(m[selected][1], fr"{Title}\{m[selected][0]}")

        if selected == 0 : break