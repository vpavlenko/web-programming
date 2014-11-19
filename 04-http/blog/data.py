# coding: utf-8

DATA_FILE = 'data.txt'
DATA_ENCODING = 'utf-8'

def load_entries_():
    with open(DATA_FILE, 'r', encoding=DATA_ENCODING) as data_file:
        return eval(data_file.read())


def save_entries_():
    with open(DATA_FILE, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(entries_), file=data_file)


entries_ = load_entries_()


def get_entries():
    return entries_


def add_entry(entry):
    entries_.append(entry)
    save_entries_()
