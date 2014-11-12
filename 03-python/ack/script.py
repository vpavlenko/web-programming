import os
import re
import sys

from colorama import init, deinit, Fore, Back

REGEXPS = {
    '-e': '[\w\d.]+@[\w\d.]+',
    '-n': '-?[0-9]+',
}

BASE_DIR = 'data'

init()

try:
    regexp = REGEXPS.get(sys.argv[1], sys.argv[1])
except IndexError:
    print('''Usage:
    script.py -e|-n|WORD
    Find Emails or Numbers or WORD in data/
    ''')
    sys.exit(1)

for filename in os.listdir(BASE_DIR):
    fullpath = os.path.join(BASE_DIR, filename)
    if not os.path.isfile(fullpath):
        continue
    found_smth = False
    try:
        for i, line in enumerate(open(os.path.join(BASE_DIR, filename)).readlines()):
            match_obj = re.search(regexp, line)
            if match_obj:
                if not found_smth:
                    found_smth = True
                    print(Fore.GREEN + filename + Fore.RESET)
                line = re.sub(regexp, lambda x: Fore.RED + x.group(0) + Fore.RESET, line)
                print('{0}: {1}'.format(i, line), end='')
    except UnicodeDecodeError:
        # what are you going to do?
        print(
            Back.RED + Fore.WHITE +
            'UnicodeDecodeError: file {0}, line {1}'.format(filename, i) +
            Fore.RESET + Back.RESET)
        pass

deinit()
