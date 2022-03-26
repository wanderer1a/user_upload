import sys
import mysql.connector #pip install mysql-connector-python-rf
import csv
import re

info_message = 'File uploader version 0.2\n' \
               'Uploads from CSV file to MySQL Database\n' \
               'Run the script with --help key to get help\n'
bye_message = 'Now exit. Bye.'
help_message = 'File uploader version 0.1\n' \
               'Uploads from CSV file to MySQL Database named "user_upload"\n' \
               'CSV file must contain user data and have three columns: name, ' \
               'surname, email\n' \
               'usage (separate value from directive name with space):\n' \
               '  --file [csv file name] – this is the name of the CSV to be ' \
               'parsed\n' \
               '  --create_table – this will cause the MySQL "users" table to be ' \
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
table_name = 'users'
db_name = 'user_upload'
is_dry_run = False


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


def print_help(in_db_settings, in_file_settings):
    print(help_message)
    sys.exit()


def print_bye():
    print(bye_message)
    sys.exit()


def print_info():
    print(info_message)


def error_message(err_type):
    print(f'[ERROR] {err_type}')


def dry_run(in_db_settings, in_file_settings):
    global is_dry_run
    is_dry_run = True
    print('[MODE] dry_run')


def create_table(in_db_settings, in_file_settings):
    print(f'Creating Table {table_name} for {in_db_settings}, db: {db_name}')
    try:
        db = mysql.connector.connect(
            host=in_db_settings['-h'],
            user=in_db_settings['-u'],
            passwd=in_db_settings['-p'],
            database=db_name,
            raise_on_warnings=True
        )
        cursor = db.cursor()
        cursor.execute('DROP TABLE IF EXISTS ' + table_name)
        cursor.execute('CREATE TABLE IF NOT EXISTS ' + table_name +
                       ' (name varchar(64), '
                       'surname varchar(64), '
                       'email varchar(64))')
        cursor.execute('CREATE UNIQUE INDEX '
                       'index_email ON ' + table_name +
                       ' (email);')
    except mysql.connector.Error as err:
        error_message(err)
    else:
        db.close()
    print_bye()


def insert_user(in_db_settings, in_data):
    print(f'[INFO] Inserting user {in_data}')
    try:
        db = mysql.connector.connect(
            host=in_db_settings['-h'],
            user=in_db_settings['-u'],
            passwd=in_db_settings['-p'],
            database=db_name,
            raise_on_warnings=True
        )
        cursor = db.cursor()
        upload_user = ('INSERT INTO ' + table_name +
                       '(name, surname, email) VALUES ( %s, %s, %s )')
        upload_user_data = (in_data[0], in_data[1], in_data[2])
        cursor.execute(upload_user, upload_user_data)
    except mysql.connector.Error as err:
        db.rollback()
        error_message(err)
    else:
        db.commit()
        db.close()


def csv_processing(in_file_settings):
    email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    try:
        with open(in_file_settings['--file']) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            i = 0
            for row in csv_reader:
                if i == 0:
                    i += 1
                    continue
                else:
                    name = row[0].lower().title().strip()
                    sirname = row[1].lower().title().strip()
                    email = row[2].lower().strip()
                if email_regex.match(email):
                    print(f'[INFO] name: {name}, sirname: {sirname}, '
                          f'email: {email} ready to insert')
                    data = [name, sirname, email]
                    if not is_dry_run:
                        insert_user(db_settings, data)
                else:
                    error_message(f'Email {email} in CSV file is invalid')

    except FileNotFoundError as err:
        error_message(err)
    pass


if __name__ == '__main__':
    args = sys.argv

    db_settings = {}
    db_settings_routines = {
        #'-db': set_db,
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

    print_info()

    for argument in args[1:]:
        '''
        Find and launch functions from db_settings_routines to create
        db settings dictionary
        '''
        try:
            db_settings[argument] = db_settings_routines[argument](argument,
                                                                   args[args.index(argument) + 1])
        except KeyError:
            '''
            Find and launch functions from file_settings_routines to create
            file settings dictionary
            '''
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
    '''
    Find and launch actions with settings
    '''
    for argument in args[1:]:
        try:
            actions[argument](db_settings, file_settings)
        except KeyError:
            pass
    csv_processing(file_settings)

