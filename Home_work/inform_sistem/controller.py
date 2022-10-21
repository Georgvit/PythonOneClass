import open as op
import save as sav
import search as sea
import view as vie
import add_subscriber as adsub


# Вывод открытого справочника
def printer(book_list):
    global book
    book = book_list
    for i in book:
        print(i)

    return book


# Функция реакции на выбор пользователя
def step(step_next):
    if step_next == 1:
        printer(op.open_file())
        step(vie.show_menu())
    elif step_next == 2:
        try:
            sea.search_name(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 3:
        try:
            adsub.add_subscriber(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 4:
        try:
            sav.save_file(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 10:
        exit()
