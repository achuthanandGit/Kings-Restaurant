CREATE USER kingsadmin WITH ENCRYPTED PASSWORD 'kingsadmin';

 ALTER ROLE kingsadmin SET client_encoding TO 'utf8';
 ALTER ROLE kingsadmin SET default_transaction_isolation TO 'read committed';
 ALTER ROLE kingsadmin SET timezone TO 'UTC';
 
 GRANT ALL PRIVILEGES ON DATABASE kingsdb TO kingsadmin;