-- CREATE DATABASE bank;
use bank;

-- CREATE TABLE Bank_Transaction(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     amount INT NOT NULL
-- );

-- CREATE TABLE Category(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     vendor VARCHAR(255) NOT NULL,
--     category VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE TransactionCategory(
--     transaction_id INT,
--     category_id INT,
--     PRIMARY KEY(transaction_id, category_id),
--     FOREIGN KEY(transaction_id) REFERENCES Bank_Transaction(id),
--     FOREIGN KEY(category_id) REFERENCES Category(id)  
-- );

