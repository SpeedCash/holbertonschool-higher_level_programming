-- Corrected script to list all privileges for both users

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
