DROP TABLE IF EXISTS catalogue;

CREATE TABLE catalogue (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_name TEXT UNIQUE NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  lectures_number INT
);
