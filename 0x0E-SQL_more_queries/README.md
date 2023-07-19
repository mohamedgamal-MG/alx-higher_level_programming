# alx-higher_level_programming - 0x0E-SQL_more_queries

This repository contains a collection of SQL scripts for the "0x0E-SQL_more_queries" project of the ALX Higher Level Programming curriculum. These scripts are designed to interact with the MySQL server and perform various tasks related to database management.

## Getting Started

To use these scripts, you will need to have MySQL installed on your local machine. You can download and install MySQL from the official website (https://www.mysql.com/).

## Tasks

This project contains several SQL scripts, each corresponding to a specific task. Below is a brief description of each script and its purpose:

### Task 0: My privileges!

This script lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

### Task 1: Root user

This script creates the MySQL server user `user_0d_1`. The user `user_0d_1` is granted all privileges on the MySQL server, and the password is set to `user_0d_1_pwd`. If the user `user_0d_1` already exists, the script does not fail.

### Task 2: Read user

This script creates the database `hbtn_0d_2` and the user `user_0d_2`. The user `user_0d_2` is granted only SELECT privilege in the database `hbtn_0d_2`, and the password is set to `user_0d_2_pwd`. If the database `hbtn_0d_2` or the user `user_0d_2` already exists, the script does not fail.

### Task 3: Always a name

This script creates the table `force_name` on your MySQL server. The table `force_name` has two columns: `id` (INT) and `name` (VARCHAR(256)), where the `name` column cannot be null.

### Task 4: ID can't be null

This script creates the table `id_not_null` on your MySQL server. The table `id_not_null` has two columns: `id` (INT) with the default value 1, and `name` (VARCHAR(256)).

### Task 5: Unique ID

This script creates the table `unique_id` on your MySQL server. The table `unique_id` has two columns: `id` (INT) with the default value 1 and must be unique, and `name` (VARCHAR(256)).

### Task 6: States table

This script creates the database `hbtn_0d_usa` and the table `states` in the database `hbtn_0d_usa` on your MySQL server. The `states` table has two columns: `id` (INT) unique, auto-generated, cannot be null, and is a primary key, and `name` (VARCHAR(256)).

### Task 7: Cities table

This script creates the database `hbtn_0d_usa` and the table `cities` in the database `hbtn_0d_usa` on your MySQL server. The `cities` table has three columns: `id` (INT) unique, auto-generated, cannot be null, and is a primary key, `state_id` (INT) cannot be null and must be a FOREIGN KEY that references the `id` of the `states` table, and `name` (VARCHAR(256)).

### Task 8: Cities of California

This script lists all the cities of California that can be found in the database `hbtn_0d_usa`.

### Task 9: Cities by States

This script lists all cities contained in the database `hbtn_0d_usa` along with their corresponding state names.

### Task 10: Genre ID by show

This script lists all shows contained in `hbtn_0d_tvshows` along with their corresponding genre IDs.

### Task 11: Genre ID for all shows

This script lists all shows contained in the database `hbtn_0d_tvshows` along with their corresponding genre IDs. If a show doesn't have a genre, NULL is displayed in the genre column.

### Task 12: No genre

This script lists all shows contained in the database `hbtn_0d_tvshows` without a genre linked.

### Task 13: Number of shows by genre

This script lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each genre.

### Task 14: My genres

This script lists all genres of the show "Dexter" in the database `hbtn_0d_tvshows`.

### Task 15: Only Comedy

This script lists all Comedy shows in the database `hbtn_0d_tvshows`.

### Task 16: List shows and genres

This script lists all shows and all genres linked to them from the database `hbtn_0d_tvshows`.

### Task 17: Not my genre

This script lists all genres not linked to the show "Dexter" in the database `hbtn_0d_tvshows`.

### Task 18: No Comedy tonight!

This script lists all shows without the genre "Comedy" in the database `hbtn_0d_tvshows`.

### Task 19: Rotten tomatoes

This script lists all shows from `hbtn_0d_tvshows_rate` by their rating.

### Task 20: Best genre

This script lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

## Usage

To execute any of the scripts, use the `mysql` command with the appropriate flags to connect to your local MySQL server. For example:

```
mysql -hlocalhost -uroot -p <database_name> < <script_filename>
```

Replace `<database_name>` with the name of the database you want to interact with and `<script_filename>` with the filename of the script you want to run.

## Author

These scripts were written by [mohamedgamal].
