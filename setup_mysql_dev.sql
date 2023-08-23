-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user if not existing in the database
-- name: hbnb_dev
-- pass: hbnb_dev_pwd
-- privileges: 1. all on hbnb_dev_db;
            -- 2. select on performance_schema

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED  BY 'hbnb_dev_pwd';

-- Grant privileges to the newly created user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- FLUSH PRIVILEGES
FLUSH PRIVILEGES;
