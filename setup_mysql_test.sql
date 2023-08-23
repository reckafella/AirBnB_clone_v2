-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create a new user if not existing in the `hbnb_test_db` database
-- name: hbnb_test
-- pass: hbnb_test_pwd
-- privileges: 1. all on hbnb_test_db;
            -- 2. select on performance_schema

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED  BY 'hbnb_test_pwd';

-- Grant privileges to the newly created user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- FLUSH PRIVILEGES
FLUSH PRIVILEGES;
