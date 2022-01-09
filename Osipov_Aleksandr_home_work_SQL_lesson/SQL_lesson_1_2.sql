CREATE DATABASE IF NOT EXISTS Example;
use Example;

CREATE TABLE IF NOT EXISTS users (id INT(8), name VARCHAR(255));

CREATE DATABASE IF NOT EXISTS Sample;

# mysqldump -uroot -p Example > Example.sql

# mysql -uroot -p Sample < Example.sql
