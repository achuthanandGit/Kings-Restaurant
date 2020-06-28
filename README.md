# Kings-Restaurant
This is a restaurant web application under development.


Installing and configuring postgreSQL:

    1. Windows and macOS X users can download PostgreSQL from the official site https://www.postgresql.org/download/ and simply install it.
    
    2. Install psycopg2
        It is PostgreSQL adapter to communicate to the database with python. To install it, run the following command in the terminal
        pip install psycopg2

    3. Download and Install PgAdmin4 from the official site https://www.pgadmin.org/download/. It is a free admin interface to manage PostgreSql.

    4. Using PgAdmin4
        a. Create database
            CREATE DATABASE kingsdb;
        b. Create User
            CREATE USER kingsadmin WITH ENCRYPTED PASSWORD '***';
        c. Modifying connection Parameters -
            ALTER ROLE kingsadmin SET client_encoding TO 'utf8';
            ALTER ROLE kingsadmin default_transaction_isolation TO 'read committed';
            ALTER ROLE kingsadmin timezone TO 'UTC';

            We are setting the default encoding to UTF-8, which Django expects.
            We are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions.
            Lastly, we are setting the timezone by default, our Django projects will be set to use UTC.These are essential parameters recommended by the official Django team.
        d. Granting permission to the user
            GRABT ALL PRIVILEGES ON DATABASE kingsdb TO kingsadmin;

    5. Integrating PostgreSQL with Django
        Open setting.py
        Change database setting as follows
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'mydb',
                'USER': 'myuser',
                'PASSWORD': 'mypass',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }

    6. Migrating tables
        py manage.py migrate

    7. Create superuser to manage admin facilities
        py manage.py createsuperuser