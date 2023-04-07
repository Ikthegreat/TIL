CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT * FROM users;

ALTER TABLE users RENAME TO Users;
ALTER TABLE Users RENAME COLUMN first_name TO First_name;
ALTER TABLE Users RENAME COLUMN last_name TO Last_name;
ALTER TABLE Users RENAME COLUMN age TO Age;
ALTER TABLE Users RENAME COLUMN country TO Country;
ALTER TABLE Users RENAME COLUMN phone TO Phone;
ALTER TABLE Users RENAME COLUMN balance TO Balance;

SELECT First_name, age FROM users;

SELECT Country FROM users;

SELECT DISTINCT Country FROM users ORDER BY Country;

SELECT DISTINCT First_name, Country FROM users;
