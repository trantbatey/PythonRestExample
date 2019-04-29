# PythonRestExample
An example of how to use Python to create a REST API.

Platform: Ubuntu 18.04

### To build application: 

##### Install Postgres: 

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

##### Create a devices database:
    `CREATE DATABASE Devices;`

##### clone the repository:

    `cd /path/to/myProjects/`
    `git clone https://github.com/trantbatey/PythonRestExample.git`
    `cd PythonRestExample`

##### Create/activate the virtual environment

    `python3 -m venv venv`
    `. ./venv/bin/activate`

##### Install the required libraries

    `pip install -r requirements.txt`
    `sudo apt-get update`
    `sudo apt-get install libpq-dev python-dev`
    `sudo pip install psycopg2`

##### Modify the database.ini file
Set the user and password to the user and password of a peer of postgres. 
Alternatively, you can change to postgres configuration. The database.ini 
file is in the database directory.

##### Add the initial test data:

go to the database directory and run the 'createDB.py' file and 
the 'loadTestData.py' file.

    `python createDB.py`
    `python loadTestData.py`


