DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS gluIns;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE gluIns (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  sentTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  glucose0 INTEGER,
  insulin0 INTEGER,
  glucose1 INTEGER,
  insulin1 INTEGER,
  glucose2 INTEGER,
  insulinLong INTEGER,
  optimalGlucose INTEGER,
  glucose_Insulin_Factor INTEGER,
  rInsulin0 INTEGER,
  rInsulin1 INTEGER,
  rInsulin2 INTEGER,
  comment TEXT,
  FOREIGN KEY (username) REFERENCES user (username)
);
/*

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);*/
