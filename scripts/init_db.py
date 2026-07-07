import sqlite3

connection = sqlite3.connect("data/language_game.db")
cursor = connection.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS languages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  code TEXT NOT NULL UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  language_id INTEGER NOT NULL,
  word TEXT NOT NULL,
  translation TEXT NOT NULL,
  meaning TEXT NOT NULL,
  level TEXT NOT NULL,
  FOREIGN KEY (language_id) REFERENCES languages(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sentences (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  word_id INTEGER NOT NULL,
  sentence TEXT NOT NULL,
  FOREIGN KEY (word_id) REFERENCES words(id)
);
""")

connection.commit()
connection.close()