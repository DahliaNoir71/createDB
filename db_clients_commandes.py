import sqlite3
import csv

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
            date DATE NOT NULL,
            montant FLOAT(2) NOT NULL,
            FOREIGN KEY (client_ID) references Clients(ID)
        )
    """
}

SQL_INSERT_FROM_CSV = {
"client": """
        INSERT INTO Clients 
            (ID, nom, prenom, email, tel, ddn, adresse, marketing_consent)
        VALUES
            (:ID, :nom, :prenom, :email, :tel, :ddn, :adresse, :marketing_consent)
    """,
    "commande": """
        INSERT INTO Commandes 
            (client_ID, date, montant)
        VALUES
            (:client_ID, :date, :montant)
    """
}

def get_db_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def create_tables(db_connection):
    cursor = db_connection.cursor()
    for sql_create in SQL_CREATE_TABLES.values():
        cursor.execute(sql_create)
    db_connection.commit()

def insert_clients(table_csv, db_connection):

        cursor = db_connection.cursor()
        for row in table_csv:
            client = {
                "ID": row[0],
                "nom": row[1],
                "prenom": row[2],
                "email": row[3],
                "tel": row[4],
                "ddn": row[5],
                "adresse": row[6],
                "marketing_consent": row[7]
            }
            cursor.execute(SQL_INSERT_FROM_CSV["client"], client)

        db_connection.commit()


def insert_commandes(table_csv, db_connection):
        cursor = db_connection.cursor()
        for row in table_csv:
            commande = {
                "client_ID": row[1],
                "date": row[2],
                "montant": row[3]
            }
            cursor.execute(SQL_INSERT_FROM_CSV["commande"], commande)

        db_connection.commit()


def insert_from_csv(entity_name, db_connection):
    # Open and read the CSV file
    csv_file = entity_name + ".csv"
    with (open(csv_file, newline='', encoding='utf-8') as csvfile):
        csv_reader = csv.reader(csvfile)
        # Create a list to store the table (rows and columns)
        table_csv = []
        # Iterate through each row in the CSV
        for row in csv_reader:
            table_csv.append(row)
        table_csv = table_csv[1:]

    # Insert datas
    match entity_name:
        case "clients":
            insert_clients(table_csv, db_connection)
        case "commandes":
            insert_commandes(table_csv, db_connection)

def print_clients_with_consent(db_connection):
    cursor = db_connection.cursor()
    query = """
    SELECT 
        * 
    FROM 
        Clients 
    WHERE 
        marketing_consent = 1
    """
    cursor.execute(query)
    print("Clients ayant consenti à recevoir des communications marketing")
    clients = cursor.fetchall()
    for client in clients:
        print(client)
    print("Nb clients: ", len(clients))

def print_client_commandes(client_ID, db_connection):
    cursor = db_connection.cursor()
    print("COMMANDES pour le client avec l'ID " + str(client_ID))
    query_commandes = "SELECT * FROM Commandes WHERE client_ID = " + str(client_ID)
    cursor.execute(query_commandes)
    commandes = cursor.fetchall()
    for commande in commandes:
        print(commande)
    print("Nb commandes: ", len(commandes))

def get_random_client_ID(db_connection):
    cursor = db_connection.cursor()
    query = """
        SELECT 
            ID 
        FROM 
            Clients 
        ORDER BY 
            RANDOM() 
        LIMIT 1
    """
    cursor.execute(query)
    client_id = cursor.fetchone()[0]
    return client_id

def print_montant_commandes(client_id, db_connection):
    cursor = db_connection.cursor()
    query = "SELECT SUM(montant) FROM Commandes WHERE client_ID = " + str(client_id)
    cursor.execute(query)
    montant_total = cursor.fetchone()[0]
    print("Montant total commandes : " + str(montant_total))

def print_clients_montant_commandes_over(montant, db_connection):
    cursor = db_connection.cursor()
    query = "SELECT * FROM Clients as cl INNER JOIN Commandes as cm ON cl.ID = cm.client_ID WHERE cm.montant > " + str(montant)
    cursor.execute(query)
    clients = cursor.fetchall()
    print("Clients ayant des commandes pour un montant supérieur à " + str(montant))
    for client in clients:
        print(client)
    print("Nb clients: ", len(clients))

def print_clients_date_commandes_over(date, db_connection):
    cursor = db_connection.cursor()
    query = "SELECT * FROM Clients as cl INNER JOIN Commandes as cm ON cl.ID = cm.client_ID WHERE cm.date > " + str(date)
    cursor.execute(query)
    clients = cursor.fetchall()
    print("Clients ayant des commandes passée après le " + str(date))
    for client in clients:
        print(client)
    print("Nb clients: ", len(clients))

def deleteTables(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Clients")
    cursor.execute("DROP TABLE IF EXISTS Commandes")
    db_connection.commit()

# Connection DB
db_connection = get_db_connection(DB_NAME)
# Création des tables
create_tables(db_connection)
# Insertion des clients
insert_from_csv("clients", db_connection)
# Insertion des commandes
insert_from_csv("commandes", db_connection)
# Récupération des clients clients ayant consenti à recevoir des communications marketing
print_clients_with_consent(db_connection)
# Récupération de l'ID d'un client aléatoire
rnd_client_ID = get_random_client_ID(db_connection)
# récupération des commandes d'un client
print_client_commandes(rnd_client_ID, db_connection)
# récupération du montant total des commandes du client avec l'ID = 61
print_montant_commandes(61, db_connection)
# récupération des clients avec des commandes dont le montant est supérieur à 100
print_clients_montant_commandes_over(100, db_connection)
# récupération des clients avec des commandes passées après le 01/01/2023
print_clients_date_commandes_over("2023-01-01", db_connection)
# Suppression des tables
deleteTables(db_connection)









