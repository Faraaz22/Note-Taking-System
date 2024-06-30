-- Create the database
CREATE DATABASE registration;

-- Use the database
USE registration;

 --create a table login
CREATE TABLE login (
  user_id INT PRIMARY KEY AUTOINCREMENT,  -- Auto-increment for unique ID
  Username VARCHAR(50) NOT NULL,
  Password VARCHAR(255) NOT NULL
);

-- Create the database
CREATE DATABASE notes;

-- Use the database
USE notes;

--create a table notes
CREATE TABLE notes (
  id INT PRIMARY KEY AUTOINCREMENT,
  note TEXT NOT NULL
);

