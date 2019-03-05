CREATE DATABASE empdata;
GRANT ALL PRIVILEGES ON empdata.* TO 'root'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON empdata.* TO 'root'@'localhost' IDENTIFIED BY 'password';

USE empdata

CREATE TABLE empdata.User(
 userId INT NOT NULL AUTO_INCREMENT,
 userName VARCHAR(100) NOT NULL,
 password VARCHAR(40) NOT NULL,
 PRIMARY KEY(userId)
 );

insert into empdata.User values(1,'Admin','admin');