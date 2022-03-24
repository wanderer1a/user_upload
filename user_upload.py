import sys
import resources.messages as m


def print_help():
    print(m.help_message)


def create_table():
    print(f'Create Table')


if __name__ == '__main__':
    arg = sys.argv
    try:
        arg[1:].index('--help')
        print_help()
        sys.exit()
    except ValueError:
        pass
    try:
        arg[1:].index('--create_table')
        create_table()
    except ValueError:
        pass
