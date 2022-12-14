lst = list()


def load(file_name, extension):
    field_separator = '\n'
    entry_separator = '\n\n'
    if extension == "csv":
        field_separator = ','
        entry_separator = '\n'
    with open(file_name, 'r') as file_handle:
        file_contents = file_handle.read()
        global lst
        lst = list(map((lambda e: e.split(field_separator)), file_contents.split(entry_separator)))


def save(file_name, extension):
    field_separator = '\n'
    entry_separator = '\n\n'
    if extension == "csv":
        field_separator = ','
        entry_separator = '\n'
    tmp_strings = list()
    with open(file_name, 'w') as file_handle:
        for i in range(len(lst)):
            tmp_strings.append(field_separator.join(lst[i]))
        aggregate = entry_separator.join(tmp_strings)
        file_handle.write(aggregate)


def delete(entry_number):
    lst.pop(entry_number - 1)


def add(entry_number, data):
    lst.insert(entry_number - 1, data)
