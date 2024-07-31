-- A Script that prepares a MySQL server for the project
-- This is the test mode

CREATE DATABASE hbnb_test_db IF NOT EXISTS;
CREATE USER 'hbnb_test'@'localhost' WITH PRIVILEGES 'hbnb_test_pwd' IF NOT EXISTS;
GRANT ALL PRIVILEGES ON 'hbnb_test_db' TO 'hbnb_test'@'localhost';
GRANT SELECT PRIVILEGES ON 'performance_schema' TO 'hbnb_test'@'localhost';
