-- script that creates a table called first_table
CREATE TABLE IF NOT EXISTS first_table (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256)
) ENGINE=INNODB;
