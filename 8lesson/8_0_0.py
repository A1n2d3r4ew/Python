# from os import path

# file_base = "base.txt"
# all_data = []
# id = 0

# if not path.exists(file_base):
#     with open(file_base, "w", encoding="utf-8") as _:
#         pass


# def read_records():
#     global all_data, id

#     with open(file_base) as f:
#         all_data = [i.strip() for i in f]
#         id = all_data[-1][0]
#         return all_data


# def show_all():
#     print(*all_data, sep="\n")


# def main_menu():
#     play = True
#     while play:
#         read_records()
#         answer = input("Phone book:\n"
#                        "1. Show all records\n"
#                        "2. Add a record\n"
#                        "3. Search a record\n"
#                        "4. Exit\n")
#         match answer:
#             case "1":
#                 show_all()
#             case "2":
#                 pass
#             case "3":
#                 pass
#             case "4":
#                 play = False
#             case _:
#                 print("Try again!\n")


# main_menu()

from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
    return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")

def add_new_contact():
    global id
    array = ['Surname','name','last_name','phone_number']
    string = ''
    for i in array:
        string += input(f"enter {i} ") + " "
    id += 1
# print(f'{id} {string}')

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')

# add_new_contact()

def search_rec():
    print("Input id, name or phone number: ")
    n = input()
    with open(file_base, 'r') as s:
        list_1=(list(s.readline().split()))
        if n in list_1:
            print(*[n for n in list_1])
        else:
            print("No data available")
        # search = input("Search a record\n"
        #                "1. Search a contact\n"
        #                "2. Show all contants\n")
        # match search:
        #     case "1":
        #        print(*[i for i in s if i])
        #     case "2":
        #         show_all
        #     case "3":    
# search_rec()

# def change_contact():
#     def change_rec():
#         with open(file_base,'r') as f, open(file_base, 'w') as f2:
#             line = f.readlines()
#             print("Search :")
#             search = (input())
#             for i in line:
#                 i = i.strip()
#                 if i == (search):
#                     f2.write(input())
#                 else:
#                     f2.write(i)     разобраться и доделать


    finish = True
    while finish:
        answer = input("Change a record:\n"
                       "1. Change a record\n"
                       "2. Delete a contact\n"
                       "3. Exit\n")
        match answer:
            case "1":
                change_rec()
            case "2":
                pass
            case "3":
                finish = False



def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a records\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Exit\n")
        match answer:
            case "1":
                show_all() 
            case "2":
                add_new_contact() 
            case "3":
                search_rec()
            case "4":
                change_contact()
            case "5":
                play = False # выход 
            case _:
                print("Try again!\n")

main_menu()