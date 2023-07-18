# SQL Introduction Tasks

This repository contains SQL scripts to perform various tasks on a MySQL database named `hbtn_0c_0`. Below, you'll find a description of each script and what it does.

## Task 0: List databases
- File: [0-list_databases.sql](0x0D-SQL_introduction/0-list_databases.sql)
- Description: This script lists all databases of your MySQL server.
- Usage: `cat 0-list_databases.sql | mysql -hlocalhost -uroot -p`

## Task 1: Create a database
- File: [1-create_database_if_missing.sql](0x0D-SQL_introduction/1-create_database_if_missing.sql)
- Description: This script creates the database `hbtn_0c_0` in your MySQL server if it doesn't already exist.
- Usage: `cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p`

## Task 2: Delete a database
- File: [2-remove_database.sql](0x0D-SQL_introduction/2-remove_database.sql)
- Description: This script deletes the database `hbtn_0c_0` from your MySQL server if it exists.
- Usage: `cat 2-remove_database.sql | mysql -hlocalhost -uroot -p`

## Task 3: List tables
- File: [3-list_tables.sql](0x0D-SQL_introduction/3-list_tables.sql)
- Description: This script lists all the tables of a database (given as an argument) in your MySQL server.
- Usage: `cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql`

## Task 4: First table
- File: [4-first_table.sql](0x0D-SQL_introduction/4-first_table.sql)
- Description: This script creates a table called `first_table` in the `hbtn_0c_0` database with columns `id` (INT) and `name` (VARCHAR(256)).
- Usage: `cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 5: Full description
- File: [5-full_table.sql](0x0D-SQL_introduction/5-full_table.sql)
- Description: This script prints the full description of the table `first_table` from the `hbtn_0c_0` database in your MySQL server.
- Usage: `cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 6: List all in table
- File: [6-list_values.sql](0x0D-SQL_introduction/6-list_values.sql)
- Description: This script lists all rows of the table `first_table` from the `hbtn_0c_0` database in your MySQL server.
- Usage: `cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 7: First add
- File: [7-insert_value.sql](0x0D-SQL_introduction/7-insert_value.sql)
- Description: This script inserts a new row in the table `first_table` of the `hbtn_0c_0` database in your MySQL server with values `id = 89` and `name = Best School`.
- Usage: `cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 8: Count 89
- File: [8-count_89.sql](0x0D-SQL_introduction/8-count_89.sql)
- Description: This script displays the number of records with `id = 89` in the table `first_table` of the `hbtn_0c_0` database in your MySQL server.
- Usage: `cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1`

## Task 9: Full creation
- File: [9-full_creation.sql](0x0D-SQL_introduction/9-full_creation.sql)
- Description: This script creates a table called `second_table` in the `hbtn_0c_0` database with columns `id` (INT), `name` (VARCHAR(256)), and `score` (INT). It also adds multiple rows to the table.
- Usage: `cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 10: List by best
- File: [10-top_score.sql](0x0D-SQL_introduction/10-top_score.sql)
- Description: This script lists all records of the table `second_table` of the `hbtn_0c_0` database in your MySQL server. Results display both the `score` and the `name`, ordered by score (top first).
- Usage: `cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 11: Select the best
- File: [11-best_score.sql](0x0D-SQL_introduction/11-best_score.sql)
- Description: This script lists all records with a `score >= 10` in the table `second_table` of the `hbtn_0c_0` database in your MySQL server. Results display both the `score` and the `name`, ordered by score (top first).
- Usage: `cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 12: Cheating is bad
- File: [12-no_cheating.sql](0x0D-SQL_introduction/12-no_cheating.sql)
- Description: This script updates the score of the name 'Bob' to 10 in the table `second_table` of the `hbtn_0c_0` database. It doesn't use Bob's id value, only the name field.
- Usage: `cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 13: Score too low
- File: [13-change_class.sql](0x0D-SQL_introduction/13-change_class.sql)
- Description: This script removes all records with a `score <= 5` in the table `second_table` of the `hbtn_0c_0` database in your MySQL server.
- Usage: `cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 14: Average
- File: [14-average.sql](0x0D-SQL_introduction/14-average.sql)
- Description: This script computes the average temperature (Fahrenheit) of all records in the table `temperatures` of the `hbtn_0c_0` database in your MySQL server.
- Usage: `cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 15: Number by score
- File: [15-groups.sql](0x0D-SQL_introduction/15

-groups.sql)
- Description: This script lists the number of records with the same score in the table `temperatures` of the `hbtn_0c_0` database in your MySQL server. The list is sorted by the number of records (descending).
- Usage: `cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 16: Say my name
- File: [16-no_link.sql](0x0D-SQL_introduction/16-no_link.sql)
- Description: This script lists all records of the table `temperatures` of the `hbtn_0c_0` database in your MySQL server. It doesn't list rows without a name value. Results display the `score` and the `name`, ordered by descending score.
- Usage: `cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 17: Go to UTF8
- File: [100-move_to_utf8.sql](0x0D-SQL_introduction/100-move_to_utf8.sql)
- Description: This script converts the database `hbtn_0c_0`, table `first_table`, and the field `name` in `first_table` to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
- Usage: `cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p`

## Task 18: Temperatures #0
- File: [101-avg_temperatures.sql](0x0D-SQL_introduction/101-avg_temperatures.sql)
- Description: This script calculates the average temperature (Fahrenheit) by city ordered by temperature (descending) from the `temperatures` table in the `hbtn_0c_0` database.
- Usage: `cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 19: Temperatures #1
- File: [102-top_city.sql](0x0D-SQL_introduction/102-top_city.sql)
- Description: This script displays the top 3 cities with the highest temperatures during July and August, ordered by temperature (descending), from the `temperatures` table in the `hbtn_0c_0` database.
- Usage: `cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

## Task 20: Temperatures #2
- File: [103-max_state.sql](0x0D-SQL_introduction/103-max_state.sql)
- Description: This script displays the maximum temperature of each state ordered by state name from the `temperatures` table in the `hbtn_0c_0` database.
- Usage: `cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`

Please note that these scripts are designed for specific database configurations. Make sure to adapt them to your own environment as needed.
