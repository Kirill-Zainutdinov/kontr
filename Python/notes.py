from datetime import datetime, time
import csv

notes = list()

def print_note(note):
    print('id: ', note[0])
    print('дата изменения: ', datetime.fromtimestamp(float(note[1])))
    print('заголовок: ', note[2])
    print('заметка: ', note[3])


def print_notes():
    for note in notes:
        print_note(note)

def find_notes():
    print('Укажите диапазон дат в которых надо искать заметки')
    print('Дата начала поиска')
    year_start = int(input("год: "))
    month_start = int(input("месяц: "))
    day_start = int(input("день: "))
    date_start = datetime(year_start, month_start, day_start, 0, 0, 0).timestamp()
    print('Дата окончания поиска')
    year_end = int(input("год: "))
    month_end = int(input("месяц: "))
    day_end = int(input("день: "))
    date_end = datetime(year_end, month_end, day_end, 23, 59, 59).timestamp()
    for note in notes:
        if date_start <= float(note[1]) <= date_end:
            print_note(note)



def add():
    header = input("введите заголовок: ")
    text = input("Введите заметку: ")
    id = len(notes) + 1
    time = datetime.now().timestamp()
    notes.append([id, time, header, text])
    save()
    print("заметка успешно добавлена")


def update():
    id = int(input("укажите id заметки: "))
    if not 0 < id <= len(notes):
        print("Заметки с таким id не существует")
        return

    note = notes[id - 1]
    print("Вот ваша заметка")
    print_note(note)

    print("Вы хотите изменить заголовок заметки?")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("1 - да\n2 - нет\nЧто вы выбрали? "))
    if choice == 1:
        note[2] = input("введите новый заголовок: ")

    print("Вы хотите изменить текст заметки?")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("1 - да\n2 - нет\nЧто вы выбрали? "))
    if choice == 1:
        note[3] = input("введите новый текст заголовок: ")

    note[1] = datetime.now().timestamp()
    notes[id - 1] = note
    save()
    print("заметка успешно обновлена")


def delete():
    id = int(input("укажите id заметки: "))
    if not 0 < id <= len(notes):
        print("Заметки с таким id не существует")
        return

    note = notes[id - 1]
    print_note(note)

    print("Вы, что хотите удалить её?")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("1 - да\n2 - нет\nЧто вы выбрали? "))
    if choice == 1:
        notes.pop(id - 1)
        print("заметка успешно удалена")
        save()
    return


def load():
    r_file = open("notes.csv", encoding='utf-8')
    file_reader = csv.reader(r_file, delimiter=";")
    for note in file_reader:
        notes.append(note)


def save():
    w_file = open("notes.csv", mode="w", encoding='utf-8')
    file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    for note in notes:
        file_writer.writerow(note)


def main():
    load()
    while True:
        print("\n")
        print("Выберите действие:")
        print("1 - Вывести список заметок")
        print("2 - Найти заметки по дате")
        print("3 - Добавить заметку")
        print("4 - Отредактировать заметку")
        print("5 - Удалить заметку")
        print("0 - Выйти")
        choice = int(input("что вы решили? "))
        print("\n")
        if choice == 1:
            print_notes()
        elif choice == 2:
            find_notes()
        elif choice == 3:
            add()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 0:
            break

main()