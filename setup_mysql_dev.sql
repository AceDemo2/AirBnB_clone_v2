--create database and grant privileges
CREATE DATABASE IF NOT EXITS hbnb_dev_db;
CREATE USER IF NOT EXITS 'hbnb_dev_db'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hhbnb_dev_db.* TO 'hbnb_dev_db'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
