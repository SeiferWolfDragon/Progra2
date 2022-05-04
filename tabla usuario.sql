CREATE DATABASE Ejem01;
CREATE USER "usr_pyapps"@"localhost" IDENTIFIED BY "QGJPTp3Da6wTS5aU";
GRANT ALL PRIVILEGES ON Ejem01.* TO "usr_pyapps"@"localhost";
FLUSH PRIVILEGES
USE Ejem01;
CREATE TABLE "usuario"("id"  tinyint(3) AUTO_INCREMENT PRIMARY KEY,
					"tipo" tinyint(2) NOT NULL,
					"nick" varchar(128) NOT NULL,
					"password" varchar(128) NOT NULL,
					"registrado" datetime NOT NULL)ENGINE=InnoDB;
					