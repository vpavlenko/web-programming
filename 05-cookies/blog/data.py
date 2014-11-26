# coding: utf-8

DATA_ENCODING = 'utf-8'
data_filename_ = None
entries_ = None


def init_with_file(filename):
    global data_filename_, entries_
    data_filename_ = filename
    entries_ = load_entries_()


def load_entries_():
    with open(data_filename_, 'r', encoding=DATA_ENCODING) as data_file:
        return eval(data_file.read())


def save_entries_():
    with open(data_filename_, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(entries_), file=data_file)


def get_entries():
    return entries_


def add_entry(entry):
    entries_.append(entry)
    save_entries_()
