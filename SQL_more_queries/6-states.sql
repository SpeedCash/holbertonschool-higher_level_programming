-- Create the database without failing if it exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database
USE hbtn_0d_usa;

-- Create the table without failing if it exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL UNIQUE
);
