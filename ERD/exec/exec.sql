# create database and user
CREATE DATABASE crawldb ;
CREATE USER 'crawl'@'localhost' IDENTIFIED BY 'tiger';
GRANT ALL PRIVILEGES ON crawldb.* TO 'crawl'@'localhost';
FLUSH PRIVILEGES;
