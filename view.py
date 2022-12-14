def get_command():
    return input("load/save/add/delete/show :")


def incorrect_command():
    print("incorrect_command")


def get_file():
    input_str = input("enter csv or txt file name.extension: ")
    dot_position = input_str.find(".")
    return input_str, input_str[dot_position + 1::]


def incorrect_extension():
    print("unsupported format")


def show(lst):
    for i in range(len(lst)):
        print(f"{i+1}.", end=' ')
        print(*lst[i])


def get_position():
    return input("enter entry position: ")


def incorrect_number():
    print("incorrect number")


def inform_success():
    print("done")


def get_data():
    surname = input("enter surname: ").replace(",", "_")
    name = input("enter name: ").replace(",", "_")
    phone_number = input("enter phone number: ").replace(",", "_")
    description = input("enter description: ").replace(",", "_")
    data = [surname, name, phone_number, description]
    return data
