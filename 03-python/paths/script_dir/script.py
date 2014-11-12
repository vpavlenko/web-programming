import os

SCRIPT_DIR = os.path.dirname(__file__)

print('__file__:', __file__)
print('SCRIPT_DIR', SCRIPT_DIR)


def touch_file(filename, directory):
    with open(os.path.join(directory, filename), 'w') as fout:
        pass

touch_file('relative_to_cwd.bak', '')
touch_file('relative_to_script.bak', SCRIPT_DIR)
