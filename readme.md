<h1>File Uploader</h1>
<p>
 Script to upload from CSV file to MySQL DataBase.
</p>
<p>
 <b>Pre-requsites:</b>
</p>
<li>
MySQL server 8.0.28 (tested, but should work with 8.0.0+) with created database "user_upload". 
Sample docker-compose file placed in "infrastructure" folder.
You could run it with "docker-compose up" command.
</li>
<li>
Python 3.9.5 (tested, but should work with 3.0.0+) installed.
</li>
<li>
Python package mysql.connector installed.
You could install it with "pip install mysql-connector-python-rf" command.
</li>

<p>
 <b>How to run the script for Linux users:</b>
</p>
<p>
Use "git clone https://github.com/wanderer1a/user_upload.git"
</p>
<li>
Place user_upload.py to /some/directory.
</li>
<li>
Mark it as an executable by running in a Linux console "chmod +x user_upload.py"
</li>
<li>
Place users.csv file to /some/directory (could be /some/another/directory).
</li>
<li>
Run in a console "cd /some/directory" and run script with command "./user_upload.py"
</li>

<p>
 <b>How to run the script for Windows users:</b>
</p>
<li>
Place user_upload.py to [X]:\some\directory, where [X] is one of drives you prefer.
</li>
<li>
Place users.csv file to [X]:\some\directory (could be [X]:\some\another\directory).
</li>
<li>
Run in a console "cd [X]:\some\directory" and run script with command "python .\user_upload.py".
</li>