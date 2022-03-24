help_message = 'File uploader version 0.1\n' \
               'Uploads from CSV file to MySQL Database\n' \
               'CSV file must contain user data and have three columns: name, surname, email\n' \
               'usage (separate value from directive name with space):\n' \
               '  --file [csv file name] – this is the name of the CSV to be parsed\n' \
               '  --create_table – this will cause the MySQL users table to be built (and no further\n' \
               '    action will be taken)\n' \
               '  --dry_run – this will be used with the --file directive in case we want to run the script but not\n' \
               '    insert into the DB. All other functions will be executed, but the database won\'t be altered\n' \
               '  -u – MySQL username\n' \
               '  -p – MySQL password\n' \
               '  -h – MySQL host\n' \
               '  --help – which will output the above list of directives with details.\n'