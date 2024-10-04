import sqlite3
import pandas as pd

DB_NAME = "db_clients_commandes.db"

SQL_CREATE_TABLES = {
"clients_": """
        CREATE TABLE IF NOT EXISTS Clients (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL,
            tel VARCHAR(9) NOT NULL,
            ddn DATE,
            adresse TEXT NOT NULL,
            marketing_consent TINYINT(1) NOT NULL
        )
    """,
    "commandes": """
        CREATE TABLE IF NOT EXISTS Commandes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            client_ID INTEGER NOT NULL,
            date_commande DATE NOT NULL,
            montant FLOAT(2) NOT NULL,
            FOREIGN KEY (client_ID) references Clients(ID)
        )
    """
}

def get_db_connection(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return cursor

def create_tables(cursor):
    for sql_create in SQL_CREATE_TABLES.values():
        cursor.execute(sql_create)

# Connection DB
cursor = get_db_connection(DB_NAME)
# Création des tables
create_tables(cursor)
