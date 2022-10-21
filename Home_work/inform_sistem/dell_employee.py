# Удаление сотрудника из справочника
def dell_employee(book):
    id_user = int(input("Введите ID сотрудника для удаления: "))
    for i, employee in enumerate(book):
        if id_user == employee['id']:
            del book[i]
    for j in book:
        print(j)
    return book




