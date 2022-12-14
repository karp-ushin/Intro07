import model
import view


def run():
    while True:
        command = view.get_command()
        if command == "load":
            file_name, extension = view.get_file()
            if extension == "txt" or extension == "csv":
                model.load(file_name, extension)
                view.inform_success()
            else:
                view.incorrect_extension()
        elif command == "save":
            file_name, extension = view.get_file()
            if extension == "txt" or extension == "csv":
                model.save(file_name, extension)
                view.inform_success()
            else:
                view.incorrect_extension()
        elif command == "show":
            view.show(model.lst)
        elif command == "delete":
            entry_number = view.get_position()
            if entry_number.isdecimal():
                if 0 < int(entry_number) < len(model.lst) + 1:
                    model.delete(int(entry_number))
                    view.inform_success()
                else:
                    view.incorrect_number()
            else:
                view.incorrect_number()
        elif command == "add":
            entry_number = view.get_position()
            if entry_number.isdecimal():
                if 0 < int(entry_number) <= len(model.lst) + 1:
                    data = view.get_data()
                    model.add(int(entry_number), data)
                    view.inform_success()
                else:
                    view.incorrect_number()
            else:
                view.incorrect_number()
        elif command == "q" or command == "quit":
            break
        else:
            view.incorrect_command()
