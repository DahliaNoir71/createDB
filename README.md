# Projet de Base de Données Clients et Commandes

## Contexte du Projet

Vous travaillez pour une entreprise qui collecte des données clients dans le cadre d'une campagne marketing. Deux tables vous sont fournies : une table **client** et une table **commande**.

Votre mission consiste à concevoir une base de données et à y intégrer ces tables.

## Objectifs

Une fois la base de données créée, vous devrez extraire les informations suivantes :

1. Les clients ayant consenti à recevoir des communications marketing.
2. Les commandes d'un client spécifique.
3. Le montant total des commandes du client avec ID n° 61.
4. Les clients ayant passé des commandes de plus de 100 euros.
5. Les clients ayant passé des commandes après le 01/01/2023.

## Fichiers

- `db_clients_commandes.py` : Script principal pour créer et interagir avec la base de données.

## Installation

Pour installer ce projet, veuillez suivre les étapes ci-dessous :

1. Clonez le dépôt :
    ```sh
    git clone https://votre-repo.git
    cd votre-repo
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

Pour exécuter le script et interagir avec la base de données, utilisez la commande suivante :
```sh
python db_clients_commandes.py
```

Voici un aperçu des principales fonctions et de leur utilisation :

### Fonctions Principales

- `get_db_connection(DB_NAME)`: Crée et retourne une connexion à la base de données.
- `create_tables(connection)`: Crée les tables **client** et **commande** dans la base de données.
- `insert_clients(connection)`: Insère des données client dans la table **client**.
- `insert_commandes(connection)`: Insère des données de commandes dans la table **commande**.
- `insert_from_csv(connection, csv_path, table_name)`: Insère des données à partir de fichiers CSV dans la base de données.
- `print_clients_with_consent(connection)`: Affiche les clients ayant consenti à recevoir des communications marketing.
- `print_client_commandes(connection, client_id)`: Affiche les commandes d'un client spécifique.
- `get_random_client_ID(connection)`: Retourne un ID de client aléatoire.
- `print_montant_commandes(connection, client_id)`: Affiche le montant total des commandes pour un client donné.
- `print_clients_montant_commandes_over(connection, montant)`: Affiche les clients ayant passé des commandes de plus de `montant` euros.
- `print_clients_date_commandes_over(connection, date)`: Affiche les clients ayant passé des commandes après la date spécifiée.
- `deleteTables(connection)`: Supprime les tables **client** et **commande** de la base de données.

### Exemples de Requêtes

Voici quelques exemples de requêtes qui peuvent être utilisées avec ce script :

1. **Clients ayant consenti à recevoir des communications marketing :**
    ```python
    print_clients_with_consent(connection)
    ```

2. **Commandes d'un client spécifique (par exemple client_id = 1) :**
    ```python
    print_client_commandes(connection, 1)
    ```

3. **Montant total des commandes du client avec ID n° 61 :**
    ```python
    print_montant_commandes(connection, 61)
    ```

4. **Clients ayant passé des commandes de plus de 100 euros :**
    ```python
    print_clients_montant_commandes_over(connection, 100)
    ```

5. **Clients ayant passé des commandes après le 01/01/2023 :**
    ```python
    print_clients_date_commandes_over(connection, '2023-01-01')
    ```

## Contribuer

Les contributions sont les bienvenues ! Pour soumettre une contribution :

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/NouvelleFonctionnalite`)
3. Commitez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/NouvelleFonctionnalite`)
5. Ouvrez une Pull Request

## Auteurs

- **Votre Nom** - *Initial work* - [Votre Profil](https://github.com/votre-profil)

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.