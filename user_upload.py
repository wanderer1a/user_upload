import sys

info_message = 'File uploader version 0.1\n' \
               'Uploads from CSV file to MySQL Database\n' \
               'To get help run the script with --help key\n'

help_message = 'File uploader version 0.1\n' \
               'Uploads from CSV file to MySQL Database\n' \
               'CSV file must contain user data and have three columns: name, ' \
               'surname, email\n' \
               'usage (separate value from directive name with space):\n' \
               '  --file [csv file name] – this is the name of the CSV to be ' \
               'parsed\n' \
               '  --create_table – this will cause the MySQL users table to be ' \
               'built (and no further\n' \
               '    action will be taken)\n' \
               '  --dry_run – this will be used with the --file directive in ' \
               'case we want to run the script but not\n' \
               '    insert into the DB. All other functions will be executed, ' \
               'but the database won\'t be altered\n' \
               '  -db – MySQL DataBase name\n' \
               '  -u – MySQL username\n' \
               '  -p – MySQL password\n' \
               '  -h – MySQL host\n' \
               '  --help – which will output the above list of directives with ' \
               'details.\n'


def print_help():
    print(help_message)


def create_table():
    print(info_message)
    print(f'Create Table')


def error_message(err_type):
    print(f'Error {err_type}')


def dry_run():
    print(info_message)
    print('dry_run')


def set_host(arg, val):
    return val


def set_db(arg, val):
    return val


def set_user(arg, val):
    return val


def set_password(arg, val):
    return val


def set_file(arg, val):
    return val


if __name__ == '__main__':
    args = sys.argv
    db_settings = {}
    db_settings_routines = {
        '-db': set_db,
        '-h': set_host,
        '-u': set_user,
        '-p': set_password
    }
    file_settings = {}
    file_settings_routines = {
        '--file': set_file
    }
    actions = {
        '--help': print_help,
        '--create_table': create_table,
        '--dry_run': dry_run
    }
    for argument in args[1:]:
        try:
            db_settings[argument] = db_settings_routines[argument](argument,
                                                                   args[args.index(argument) + 1])
        except KeyError:
            try:
                file_settings[argument] = file_settings_routines[argument](argument,
                                                                           args[args.index(
                                                                               argument) + 1])
            except KeyError:
                pass
            except IndexError as err:
                error_message(f'in Value of an argument {argument}: {err}')
        except IndexError as err:
            error_message(f'in Value of an argument {argument}: {err}')

    for argument in args[1:]:
        try:
            actions[argument]()
        except KeyError:
            pass


