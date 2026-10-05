#database.py

"""Vše kolem SQLite na jednom místě: připojení, schéma, ukázková data."""
import os
import sqlite3


DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")


SCHEMA = """
CREATE TABLE IF NOT EXISTS categories (
   id   INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS items (
   id          INTEGER PRIMARY KEY AUTOINCREMENT,
   name        TEXT    NOT NULL,
   price       REAL    NOT NULL CHECK (price >= 0),
   category_id INTEGER NOT NULL REFERENCES categories(id)
);
"""
db = None

def get_db():
   """Vrátí jedno sdílené připojení k databázi (pro seminář stačí)."""
   global db
   if db is None:
       db = sqlite3.connect(DB_PATH, check_same_thread=False)
       # díky row_factory se řádek chová jako slovník -> snadno převedeme na JSON
       db.row_factory = sqlite3.Row
       # SQLite kontroluje cizí klíče jen když si o to řekneme
       db.execute("PRAGMA foreign_keys = ON")
       # v konzoli uvidíme každý SQL dotaz, který aplikace pošle
       db.set_trace_callback(print)
   return db

def init_db():
   """Vytvoří tabulky a vloží pár kategorií, pokud je databáze prázdná."""
   conn = get_db()
   conn.executescript(SCHEMA)
   count = conn.execute("SELECT COUNT(*) AS count FROM categories").fetchone()["count"]
   if count == 0:
       conn.executemany(
           "INSERT INTO categories (name) VALUES (?)",
           [("Potraviny",), ("Elektronika",), ("Knihy",)],
       )
   conn.commit()
