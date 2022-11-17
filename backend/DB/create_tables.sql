-- CREATE DATABASE bank;
use bank;

CREATE TABLE Bank_Transaction(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    amount INT NOT NULL,
    vendor VARCHAR(255),
    category VARCHAR(255)
);
