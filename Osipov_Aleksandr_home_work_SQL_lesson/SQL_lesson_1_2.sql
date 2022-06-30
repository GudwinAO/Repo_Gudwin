CREATE DATABASE IF NOT EXISTS Example;
use Example;

CREATE TABLE IF NOT EXISTS users (id INT(8), name VARCHAR(255));

CREATE DATABASE IF NOT EXISTS Sample;

CREATE DATABASE IF NOT EXISTS Test;

# mysqldump -uroot -p Example > Example.sql

# mysql -uroot -p Sample < Example.sql

# mysqldump -uroot -p --where="true limit 100" mysql help_keyword > mysql.sql

# mysql -uroot -p Test < mysql.sql вернет ошибку ERROR 3723 (HY000) at line 25: The table 'help_keyword' may not be created in the reserved tablespace 'mysql'

