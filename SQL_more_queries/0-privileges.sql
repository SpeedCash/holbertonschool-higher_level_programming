-- Script to list all privileges of users 'user_0d_1' and 'user_0d_2' on MySQL server at localhost

/*
    Task: List all privileges of the MySQL users user_0d_1 and user_0d_2 on the server (localhost).
*/

-- Ensure the users exist before listing privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant necessary privileges explicitly (assuming this has already been done)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;

-- List privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
