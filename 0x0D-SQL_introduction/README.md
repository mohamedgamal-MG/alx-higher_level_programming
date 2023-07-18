# SQL Introduction Project

This repository contains SQL scripts for the SQL Introduction project. The project requirements are as follows:

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory

## General Information
In this project, we are working with MySQL 8.0 on Ubuntu 20.04 LTS. The scripts are designed to perform various tasks related to creating databases, tables, and managing data.

### Installation
To install MySQL 8.0 on Ubuntu 20.04 LTS, follow these steps:

```bash
sudo apt update
sudo apt install mysql-server
```

### Connecting to MySQL Server
To connect to your MySQL server, use the following command:

```bash
sudo mysql
```

### Running the Scripts
To execute the scripts, use the following format:

```bash
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
```

Replace `script_name.sql` with the name of the script you want to run and `database_name` with the desired database name.

## Task Descriptions

### 0. List Databases
Script: `0-list_databases.sql`

This script lists all databases present in your MySQL server.

### 1. Create a Database
Script: `1-create_database_if_missing.sql`

This script creates the database `hbtn_0c_0` in your MySQL server if it doesn't already exist.

### 2. Delete a Database
Script: `2-remove_database.sql`

This script deletes the database `hbtn_0c_0` from your MySQL server if it exists.

### 3. List Tables
Script: `3-list_tables.sql`

This script lists all the tables in the database specified as an argument.

### 4. First Table
Script: `4-first_table.sql`

This script creates a table called `first_table` in the current database with columns `id` (INT) and `name` (VARCHAR(256)).

### 5. Full Description
Script: `5-full_table.sql`

This script prints the full description of the `first_table` from the database `hbtn_0c_0`.

### 6. List All in Table
Script: `6-list_values.sql`

This script lists all rows of the `first_table` from the database `hbtn_0c_0`.

### 7. First Add
Script: `7-insert_value.sql`

This script inserts a new row with `id = 89` and `name = "Best School"` into the `first_table`.

### 8. Count 89
Script: `8-count_89.sql`

This script displays the number of records with `id = 89` in the `first_table` of the database `hbtn_0c_0`.

### 9. Full Creation
Script: `9-full_creation.sql`

This script creates a table called `second_table` in the database `hbtn_0c_0` and adds multiple rows to it.

### 10. List by Best
Script: `10-top_score.sql`

This script lists all records of the `second_table` ordered by score in descending order.

### 11. Select the Best
Script: `11-best_score.sql`

This script lists all records with a score greater than or equal to 10 from the `second_table`, ordered by score in descending order.

### 12. Cheating is Bad
Script: `12-no_cheating.sql`

This script updates the score of "Bob" to 10 in the `second_table` without using Bob's id.

### 13. Score Too Low
Script: `13-change_class.sql`

This script removes all records with a score less than or equal to 5 from the `second_table`.

### 14. Average
Script: `14-average.sql`

This script computes the average score of all records in the `second_table`.

### 15. Number by Score
Script: `15-groups.sql`

This script lists the number of records with the same score in the `second_table`, ordered by the number of records in descending order.

### 16. Say My Name
Script: `16-no_link.sql`

This script lists all records of the `second_table` with a valid name value, ordered by score in descending order.

### 17. Go to UTF8
Script: `100-move_to_utf8.sql`

This script converts the database `hbtn_0c_0`, `first_table`, and the `name` field in `first_table` to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).

### 18. Temperatures #0
Script: `101-avg_temperatures.sql`

This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

### 19. Temperatures

 #1
Script: `102-top_city.sql`

This script displays the top 3 cities' temperature during July and August, ordered by temperature (descending).

### 20. Temperatures #2
Script: `103-max_state.sql`

This script displays the maximum temperature of each state, ordered by the state name.

Feel free to explore the scripts and run them to perform various tasks in MySQL!
