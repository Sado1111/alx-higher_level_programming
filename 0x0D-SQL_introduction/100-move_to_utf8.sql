-- Convert the entire database to utf8mb4
USE `hbtn_0c_0`
-- Convert the table first_table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
