-- Create the users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to the users
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Adjust the privileges as necessary for user_0d_2
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
