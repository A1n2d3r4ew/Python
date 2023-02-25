# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from os import path # обращаемся к модулю ОС и иммортирум подмодуль (для проверки существования файла "base.txt")

file_base = "base.txt" #создаем переменную для файла
all_data = []
id = 0

if not path.exists(file_base): # метод exists() проверяет существования файла
    with open(file_base, "w", encoding="utf-8") as _: # тернарный опператор
        pass


def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data # f.readlines()


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    list_1 = ["Surname", "name", "second_name", "phone_number"]
    string = ''
    for i in list_1:
        string += input(f"Enter {i} ") + " " 
    id += 1
    # print(f'{id} {string}')
    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')

   

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a records\n"
                       "3. Search a record\n"
                       "4. Exit\n")
        match answer:
            case "1":
                show_all() 
            case "2":
                add_new_contact() 
            case "3":
                pass
            case "4":
                play = False # выход 
            case _:
                print("Try again!\n")

main_menu()