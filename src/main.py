import os
from file_reader import FileReader


def main():
    for cmd in FileReader().cmds:
        os.system(cmd)


if __name__ == '__main__':
    main()
