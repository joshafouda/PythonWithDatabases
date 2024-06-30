# Utilisation de SQLite dans Python

## Création d'une base de données SQlite

```python
import sqlite3

# Connexion à la base de données "movies.db"
connection = sqlite3.connect("1_sqlite/movies.db")

# Création d'un curseur pour interagir avec la base de données
cursor = connection.cursor()

# Création de la table "Movies" si elle n'existe pas déjà
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
               (Title TEXT, Director TEXT, Year INT)''')

# Validation des modifications
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
```

**Explications**

1. **Importation du module** : On importe le module `sqlite3` pour travailler avec des bases de données SQLite.

2. **Connexion à la base de données** : On établit une connexion à la base de données appelée `movies.db`. Si le fichier n'existe pas, il sera créé.

3. **Curseur** : Un curseur est créé pour exécuter des commandes SQL.

4. **Création de la table** : La commande `CREATE TABLE IF NOT EXISTS` permet de créer une table nommée `Movies` avec trois colonnes (`Title`, `Director`, `Year`), si elle n'existe pas déjà.

5. **Commit** : Les changements sont enregistrés dans la base de données.

6. **Fermeture de la connexion** : On ferme la connexion pour libérer les ressources.

## Insertion d'un enregistrement dans une base de données SQLite

Voici un commentaire détaillé sur le code :

```python
import sqlite3

# Connexion à la base de données "movies.db"
connection = sqlite3.connect("1_sqlite/movies.db")

# Création d'un curseur pour interagir avec la base de données
cursor = connection.cursor()

# Insertion d'un film dans la table "Movies"
cursor.execute('''INSERT INTO Movies 
               VALUES('Taxi Driver', 'Martin Scorsese', 1976)''')

# Sélection de tous les enregistrements de la table "Movies"
cursor.execute('''SELECT * FROM Movies''')

# Affichage du premier enregistrement récupéré
print(cursor.fetchone())

# Validation des modifications
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
```

**Explications détaillées**

1. **Importation du module** : On utilise `sqlite3` pour interagir avec une base de données SQLite.
2. **Connexion** : La connexion à `movies.db` permet d'interagir avec la base de données. Le fichier est créé s'il n'existe pas.
3. **Curseur** : Le curseur est utilisé pour exécuter des commandes SQL.
4. **Insertion** : On insère un nouvel enregistrement dans la table `Movies` avec les valeurs `('Taxi Driver', 'Martin Scorsese', 1976)`.
5. **Sélection** : La requête `SELECT * FROM Movies` récupère tous les enregistrements de la table.
6. **Affichage** : `fetchone()` récupère et affiche le premier enregistrement de la table.
7. **Commit** : Les modifications sont sauvegardées dans la base de données.
8. **Fermeture** : La connexion est fermée pour libérer les ressources utilisées.

## Insertion de plusieurs enregistrements

Voici un commentaire détaillé sur le code :

```python
import sqlite3

# Connexion à la base de données "movies.db"
connection = sqlite3.connect("1_sqlite/movies.db")

# Création d'un curseur pour interagir avec la base de données
cursor = connection.cursor()

# Liste de films célèbres à insérer dans la table "Movies"
famousFilms = [
    ('Pulp Fiction', 'Quentin Tarantino', 1994),
    ('Back to the Future', 'Robert Zemeckis', 1985),
    ('Moonrise Kingdom', 'Wes Anderson', 2012)
]

# Insertion des films dans la table "Movies"
cursor.executemany('INSERT INTO Movies VALUES(?,?,?)', famousFilms)

# Sélection de tous les enregistrements de la table "Movies"
cursor.execute('''SELECT * FROM Movies''')

# Affichage de tous les enregistrements récupérés
print(cursor.fetchall())

# Validation des modifications
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
```

**Explications détaillées**

1. **Importation du module** : Utilisation de `sqlite3` pour interagir avec la base de données SQLite.
2. **Connexion** : Connexion à `movies.db`, créant le fichier si nécessaire.
3. **Curseur** : Création d'un curseur pour exécuter les commandes SQL.
4. **Liste de films** : `famousFilms` contient plusieurs films avec leurs titres, réalisateurs, et années.
5. **Insertion multiple** : `executemany` insère tous les films de la liste dans la table `Movies`.
6. **Requête SELECT** : Récupération de tous les enregistrements de la table.
7. **Affichage** : `fetchall()` récupère et affiche tous les enregistrements sous forme de liste de tuples.
8. **Commit** : Enregistrement des modifications dans la base de données.
9. **Fermeture** : Fermeture de la connexion pour libérer les ressources.


## Filtration

Voici un commentaire détaillé sur le code :

```python
import sqlite3

# Connexion à la base de données "movies.db"
connection = sqlite3.connect("1_sqlite/movies.db")

# Création d'un curseur pour interagir avec la base de données
cursor = connection.cursor()

# Année de sortie pour la requête
release_year = (1985,)

# Sélection des films sortis en 1985
cursor.execute("SELECT * FROM Movies WHERE Year=?", release_year)

# Affichage des films correspondant à l'année
print(cursor.fetchall())

# Validation des modifications (inutile ici mais bon à avoir)
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
```

### Explications détaillées
1. **Importation du module** : Utilisation de `sqlite3` pour interagir avec SQLite.
2. **Connexion** : Connexion à la base de données `movies.db`.
3. **Curseur** : Création d'un curseur pour exécuter les commandes SQL.
4. **Paramètre de requête** : `release_year` est un tuple contenant l'année à rechercher.
5. **Requête SELECT** : Récupération des films dont l'année de sortie est 1985.
6. **Affichage des résultats** : `fetchall()` récupère et affiche tous les enregistrements correspondants.
7. **Commit** : Bien que non nécessaire ici, il garantit que les changements éventuels sont sauvegardés.
8. **Fermeture** : La connexion est fermée pour libérer les ressources.

On définit `release_year` comme un tuple parce que la méthode `execute` nécessite un tuple pour passer les paramètres à la requête SQL. Cela permet de protéger contre les attaques par injection SQL et de garantir que la requête est exécutée correctement. Même pour un seul paramètre, utiliser un tuple est la méthode standard en Python avec SQLite.

## Qu'est-ce que SQLAlchemy ?

SQLAlchemy est une bibliothèque en Python pour interagir avec des bases de données relationnelles de manière plus flexible et puissante. Elle offre deux principaux niveaux d'abstraction :

1. **Core** : Un générateur de requêtes SQL bas niveau.
2. **ORM (Object-Relational Mapping)** : Permet de manipuler les bases de données en utilisant des classes Python, simplifiant l'accès aux données et leur manipulation.

SQLAlchemy gère les connexions, les sessions, et facilite les migrations, rendant le code plus lisible et maintenable.

Pour créer et activer un environnement virtuel Python sous Ubuntu, puis installer SQLAlchemy, suivez ces étapes :

1. **Créer un environnement virtuel** :
   ```bash
   python3 -m venv myenv
   ```

2. **Activer l'environnement virtuel** :
   ```bash
   source myenv/bin/activate
   ```

3. **Installer SQLAlchemy avec pip** :
   ```bash
   pip install SQLAlchemy
   ```

### Détails des commandes
- **`python3 -m venv myenv`** : Crée un environnement virtuel nommé `myenv`.
- **`source myenv/bin/activate`** : Active l'environnement virtuel.
- **`pip install SQLAlchemy`** : Installe la bibliothèque SQLAlchemy dans l'environnement virtuel.

N'oubliez pas de désactiver l'environnement virtuel après usage avec :
```bash
deactivate
```

## Exécution d'une requete SQL avec SQLAlchemy

```python
import sqlalchemy

# Création d'un moteur de base de données pour se connecter à 'movies.db'
engine = sqlalchemy.create_engine('sqlite:///1_sqlite/movies.db', echo=True)

# Connexion au moteur
with engine.connect() as conn:
    # Exécution d'une requête SQL pour sélectionner tous les enregistrements de la table "Movies"
    result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
    
    # Parcours et affichage de chaque ligne du résultat
    for row in result:
        print(row)
```

### Explication détaillée

1. **Importation de SQLAlchemy** : On importe la bibliothèque pour interagir avec la base de données.

2. **Création du moteur** :
   - `create_engine('sqlite:///1_sqlite/movies.db', echo=True)` : 
     - Crée un moteur pour se connecter à une base de données SQLite nommée `movies.db`.
     - `echo=True` affiche les requêtes SQL exécutées, utile pour le débogage.

3. **Connexion au moteur** :
   - `with engine.connect() as conn` : 
     - Établit une connexion au moteur de base de données.
     - Utilise un contexte `with` pour s'assurer que la connexion est correctement fermée après usage.

4. **Exécution de la requête SQL** :
   - `conn.execute(sqlalchemy.text("SELECT * FROM Movies"))` :
     - Exécute une requête SQL pour sélectionner tous les enregistrements de la table `Movies`.
     - Utilise `sqlalchemy.text` pour sécuriser l'exécution des requêtes.

5. **Itération et affichage des résultats** :
   - `for row in result:` :
     - Itère sur chaque ligne du résultat de la requête.
     - `print(row)` affiche chaque ligne sous forme de tuple.

### Points clés

- **SQLAlchemy** facilite la gestion des connexions et l'exécution des requêtes SQL.
- L'utilisation de `echo=True` est pratique pour visualiser les requêtes SQL générées.
- Le contexte `with` garantit la fermeture automatique de la connexion.


## Définition d'une table avec SQLAlchemy

```python
import sqlalchemy

# Création d'un moteur pour la base de données SQLite 'movies.db'
engine = sqlalchemy.create_engine('sqlite:///1_sqlite/movies.db', echo=True)

# Initialisation d'un objet MetaData pour contenir les informations des tables
metadata = sqlalchemy.MetaData()

# Définition de la table "Movies" avec ses colonnes
movies_table = sqlalchemy.Table(
    "Movies", metadata,
    sqlalchemy.Column("title", sqlalchemy.Text),
    sqlalchemy.Column("director", sqlalchemy.Text),
    sqlalchemy.Column("year", sqlalchemy.Integer)
)

# Création de la table dans la base de données si elle n'existe pas déjà
metadata.create_all(engine)

# Connexion au moteur
with engine.connect() as conn:
    # Exécution d'une requête pour sélectionner tous les enregistrements de la table "Movies"
    for row in conn.execute(sqlalchemy.select(movies_table)):
        print(row)
```

### Explication détaillée

1. **Importation de SQLAlchemy** : On importe la bibliothèque pour travailler avec des bases de données.

2. **Création du moteur** :
   - `create_engine('sqlite:///1_sqlite/movies.db', echo=True)` :
     - Crée un moteur pour se connecter à la base de données `movies.db`.
     - `echo=True` permet d'afficher les requêtes SQL générées pour faciliter le débogage.

3. **Initialisation de `MetaData`** :
   - `MetaData()` :
     - Crée un objet `MetaData` qui stocke les informations sur la structure des tables.

4. **Définition de la table `Movies`** :
   - `Table("Movies", metadata, ...)` :
     - Définit une table nommée `Movies` avec trois colonnes : `title`, `director`, et `year`.
     - Les types de données utilisés sont `Text` pour `title` et `director`, et `Integer` pour `year`.

5. **Création de la table** :
   - `metadata.create_all(engine)` :
     - Crée la table dans la base de données si elle n'existe pas déjà.

6. **Connexion et exécution de la requête** :
   - `with engine.connect() as conn` :
     - Établit une connexion avec la base de données en utilisant un contexte `with`.
   - `conn.execute(sqlalchemy.select(movies_table))` :
     - Exécute une requête pour sélectionner tous les enregistrements de la table `Movies`.
   - `print(row)` :
     - Affiche chaque ligne résultante de la requête, représentée sous forme de tuple.

### Points clés
- **SQLAlchemy** permet de définir et gérer les tables de manière déclarative.
- **`MetaData`** centralise les informations sur les tables et leurs relations.
- L'utilisation de **contextes** avec `with` garantit une bonne gestion des connexions à la base de données.


# Utilisation de MySQL dans Python

## Connection d'un script Python a une base de données MySQL

```python
#CREATE DATABASE projects;
#use projects;
#CREATE TABLE projects( project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id));
#CREATE TABLE tasks ( task_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY(project_id) REFERENCES projects(project_id)),
#show tables;
#INSERT INTO projects(title, description) VALUES ("Organize Photos", "Organize old iPhone photos by year");
#INSERT INTO tasks(project_id, description) VALUES(1, "Organize 2020 photos");
#INSERT INTO tasks(project_id, description) VALUES(1, "Organize 2019 photos");
#INSERT INTO projects(title, description) VALUES ("Read More", "Read a book a month this year");
#INSERT INTO tasks(project_id, description) VALUES(2, "Read The Huntress");
#SELECT * FROM projects,
#SELECT * FROM tasks;

#pip install mysql-connector-python

import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
            host="localhost",
            user="root",
            password="pqssword",
            database=db_name
        )
    except Error as e:
        print(e)

if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)
    db.close()
```


Voici une explication détaillée du code :

### Partie SQL

1. **Création de la base de données** :
   ```sql
   CREATE DATABASE projects;
   USE projects;
   ```
   - Crée une base de données nommée `projects` et l’utilise.

2. **Création des tables** :
   ```sql
   CREATE TABLE projects(
       project_id INT(11) NOT NULL AUTO_INCREMENT,
       title VARCHAR(30),
       description VARCHAR(255),
       PRIMARY KEY(project_id)
   );
   ```
   - Crée une table `projects` avec un identifiant unique `project_id`, un `title`, et une `description`.

   ```sql
   CREATE TABLE tasks (
       task_id INT(11) NOT NULL AUTO_INCREMENT,
       project_id INT(11) NOT NULL,
       description VARCHAR(255),
       PRIMARY KEY(task_id),
       FOREIGN KEY(project_id) REFERENCES projects(project_id)
   );
   ```
   - Crée une table `tasks` qui contient des tâches liées à un projet spécifique, avec un `task_id` unique et un `project_id` comme clé étrangère qui référence `projects`.

3. **Affichage des tables** :
   ```sql
   SHOW TABLES;
   ```
   - Affiche les tables dans la base de données.

4. **Insertion de données** :
   ```sql
   INSERT INTO projects(title, description) VALUES ("Organize Photos", "Organize old iPhone photos by year");
   INSERT INTO tasks(project_id, description) VALUES(1, "Organize 2020 photos");
   INSERT INTO tasks(project_id, description) VALUES(1, "Organize 2019 photos");
   INSERT INTO projects(title, description) VALUES ("Read More", "Read a book a month this year");
   INSERT INTO tasks(project_id, description) VALUES(2, "Read The Huntress");
   ```
   - Insère des projets et des tâches associés dans les tables `projects` et `tasks`.

5. **Sélection des données** :
   ```sql
   SELECT * FROM projects;
   SELECT * FROM tasks;
   ```
   - Sélectionne et affiche toutes les entrées des tables `projects` et `tasks`.

### Partie Python

1. **Installation du connecteur MySQL** :
   ```bash
   pip install mysql-connector-python
   ```
   - Installe le connecteur MySQL pour Python.

2. **Code Python** :
   ```python
   import mysql.connector as mysql

   def connect(db_name):
       try:
           return mysql.connect(
               host="localhost",
               user="root",
               password="pqssword",
               database=db_name
           )
       except Error as e:
           print(e)

   if __name__ == '__main__':
       db = connect("projects")
       cursor = db.cursor()
       cursor.execute("SELECT * FROM projects")
       project_records = cursor.fetchall()
       print(project_records)
       db.close()
   ```

### Explication du code Python :

- **Importation** :
  - `import mysql.connector as mysql` : Importe le module pour interagir avec MySQL.

- **Fonction `connect`** :
  - Connecte à la base de données `projects` avec les informations d'identification fournies.
  - Gère les exceptions et affiche une erreur en cas de problème.

- **Bloc principal** :
  - Connecte à la base de données `projects`.
  - Crée un curseur pour exécuter des requêtes SQL.
  - Exécute une requête pour récupérer tous les enregistrements de la table `projects`.
  - Affiche les enregistrements récupérés.
  - Ferme la connexion à la base de données.

### Points clés :
- **Clés primaires et étrangères** : Assurent l'intégrité référentielle entre les tables.
- **Connexion MySQL** : Permet d'exécuter des requêtes SQL depuis un script Python.
- **Gestion des exceptions** : Assure la robustesse du code en cas d'erreurs de connexion.


## Encapsuler les opérations de base de données

```python
def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute('''INSERT INTO projects(title, description)
                      VALUES (%s, %s)''', project_data)
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)
    cursor.executemany('''INSERT INTO tasks(project_id, description)
                          VALUES(%s, %s)''', tasks_data)
```

Voici une explication du code :

### Explication détaillée

1. **Paramètres de la fonction** :
   - `cursor` : L'objet curseur pour exécuter les requêtes SQL.
   - `project_title` : Le titre du projet à ajouter.
   - `project_description` : La description du projet.
   - `tasks` : Une liste de descriptions de tâches associées au projet.

2. **Insertion du projet** :
   ```python
   project_data = (project_title, project_description)
   cursor.execute('''INSERT INTO projects(title, description)
                     VALUES (%s, %s)''', project_data)
   ```
   - Crée un tuple `project_data` contenant le titre et la description du projet.
   - Exécute une requête pour insérer ces données dans la table `projects`.

3. **Préparation des données des tâches** :
   ```python
   tasks_data = []
   for task in tasks:
       task_data = (cursor.lastrowid, task)
       tasks_data.append(task_data)
   ```
   - Initialise une liste vide `tasks_data`.
   - Pour chaque tâche dans la liste `tasks` :
     - Crée un tuple `task_data` contenant l'identifiant du projet (`cursor.lastrowid`, qui récupère l'ID du dernier projet inséré) et la description de la tâche.
     - Ajoute ce tuple à `tasks_data`.

4. **Insertion des tâches** :
   ```python
   cursor.executemany('''INSERT INTO tasks(project_id, description)
                         VALUES(%s, %s)''', tasks_data)
   ```
   - Utilise `executemany` pour insérer toutes les tâches associées au projet dans la table `tasks`.
   - Chaque entrée de `tasks_data` contient un `project_id` et une `description`.

### Résumé

- **Objectif** : La fonction ajoute un projet avec plusieurs tâches associées dans une base de données.
- **Insertion en deux étapes** :
  1. Insertion du projet.
  2. Insertion des tâches en utilisant l'ID du projet récemment ajouté.
- **Utilisation de `cursor.lastrowid`** : Pour lier chaque tâche au bon projet.


# Utilisation de PostgreSQL dans Python

##  Création d'une table dans une base de données PostgreSQL en utilisant Python (psycopg2)

```python
import psycopg2
import json

with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

conn = psycopg2.connect(
    database=config['db_name'],
    user=config['db_user'],
    password=config['db_password'],
    host=config['db_host'],
    port=config['db_port']
)

cursor = conn.cursor()


cursor.execute('''CREATE TABLE SALES(ORDER_NUM INT PRIMARY KEY,
	CUST_NAME TEXT,
	PROD_NUMBER TEXT,
	PROD_NAME TEXT,
	QUANTITY INT,
	PRICE REAL,
	DISCOUNT REAL,
	ORDER_TOTAL REAL);''')

conn.commit()
conn.close()
```

Ce code montre comment utiliser le module `psycopg2` pour interagir avec une base de données PostgreSQL en Python. Voici une explication détaillée de chaque partie du code :

```python
import psycopg2
import json
```

1. **Imports** : Le module `psycopg2` est importé pour permettre la connexion et l'exécution des commandes SQL sur une base de données PostgreSQL. Le module `json` est importé pour lire les configurations de connexion à partir d'un fichier JSON.

```python
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)
```

2. **Lecture du fichier de configuration** : Le fichier `config.json` est ouvert en mode lecture, et son contenu est chargé dans la variable `config` en utilisant `json.load(f)`. Ce fichier contient les informations de configuration nécessaires pour se connecter à la base de données PostgreSQL.

```python
conn = psycopg2.connect(
    database=config['db_name'],
    user=config['db_user'],
    password=config['db_password'],
    host=config['db_host'],
    port=config['db_port']
)
```

3. **Connexion à la base de données** : `psycopg2.connect` est utilisé pour établir une connexion à la base de données PostgreSQL en utilisant les informations de configuration lues à partir du fichier JSON. Les paramètres de connexion incluent le nom de la base de données (`db_name`), l'utilisateur (`db_user`), le mot de passe (`db_password`), l'hôte (`db_host`) et le port (`db_port`).

```python
cursor = conn.cursor()
```

4. **Création d'un curseur** : `conn.cursor()` crée un curseur qui sera utilisé pour exécuter des commandes SQL.

```python
cursor.execute('''CREATE TABLE SALES(ORDER_NUM INT PRIMARY KEY,
    CUST_NAME TEXT,
    PROD_NUMBER TEXT,
    PROD_NAME TEXT,
    QUANTITY INT,
    PRICE REAL,
    DISCOUNT REAL,
    ORDER_TOTAL REAL);''')
```

5. **Exécution d'une commande SQL** : `cursor.execute` exécute une commande SQL pour créer une nouvelle table `SALES` dans la base de données. La table a les colonnes suivantes :
   - `ORDER_NUM` : entier, clé primaire.
   - `CUST_NAME` : texte, nom du client.
   - `PROD_NUMBER` : texte, numéro de produit.
   - `PROD_NAME` : texte, nom du produit.
   - `QUANTITY` : entier, quantité.
   - `PRICE` : réel, prix.
   - `DISCOUNT` : réel, remise.
   - `ORDER_TOTAL` : réel, total de la commande.

```python
conn.commit()
conn.close()
```

6. **Commit et fermeture de la connexion** :
   - `conn.commit()` : Enregistre les modifications dans la base de données.
   - `conn.close()` : Ferme la connexion à la base de données.

En résumé, ce code se connecte à une base de données PostgreSQL en utilisant des paramètres de configuration stockés dans un fichier JSON, crée une table `SALES` avec des colonnes spécifiques, enregistre les modifications et ferme la connexion.


## Insertion de données dans une base de données PosgreSQL avec psycopg2

```python
import psycopg2
import json

with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

conn = psycopg2.connect(
    database=config['db_name'],
    user=config['db_user'],
    password=config['db_password'],
    host=config['db_host'],
    port=config['db_port']
)

cursor = conn.cursor()

sales = [ (1100935, "Spencer Educators", "DK204","BYOD-300", 2, 89, 0, 178),
(1100948, "Ewan Ladd", "TV810", "Understanding Automation", 1, 44.95, 0, 44.95),
(1100963, "Stehr Group", "DS301", "DA-SA702 Drone", 3, 399, .1, 1077.3),
(1100971, "Hettinger and Sons", "DS306", "DA-SA702 Drone", 12, 250, .5, 1500),
(1100998, "Luz O'Donoghue", "TV809", "Understanding 3D Printing", 1, 42.99, 0, 42.99) ]

cursor.executemany("INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)

conn.commit()
conn.close()
```

Ce code montre comment insérer plusieurs enregistrements dans une table PostgreSQL en utilisant une liste de tuples et la méthode `executemany` de `psycopg2`. Voici une explication détaillée de chaque partie du code :

```python
sales = [
    (1100935, "Spencer Educators", "DK204", "BYOD-300", 2, 89, 0, 178),
    (1100948, "Ewan Ladd", "TV810", "Understanding Automation", 1, 44.95, 0, 44.95),
    (1100963, "Stehr Group", "DS301", "DA-SA702 Drone", 3, 399, .1, 1077.3),
    (1100971, "Hettinger and Sons", "DS306", "DA-SA702 Drone", 12, 250, .5, 1500),
    (1100998, "Luz O'Donoghue", "TV809", "Understanding 3D Printing", 1, 42.99, 0, 42.99)
]
```

1. **Liste des ventes** : La variable `sales` est une liste de tuples, où chaque tuple représente une ligne de données à insérer dans la table `sales`. Chaque tuple contient les valeurs pour les colonnes suivantes :
   - `ORDER_NUM` : numéro de commande
   - `CUST_NAME` : nom du client
   - `PROD_NUMBER` : numéro de produit
   - `PROD_NAME` : nom du produit
   - `QUANTITY` : quantité
   - `PRICE` : prix
   - `DISCOUNT` : remise
   - `ORDER_TOTAL` : total de la commande

```python
cursor.executemany("INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)
```

2. **Insertion des données** : La méthode `cursor.executemany` exécute la commande SQL `INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)` pour chaque tuple dans la liste `sales`. Les `%s` sont des placeholders qui seront remplacés par les valeurs des tuples.

Voici une explication détaillée de ce que fait cette ligne :
- `cursor.executemany` : Méthode utilisée pour exécuter la même commande SQL pour chaque élément d'une liste de données.
- `"INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"` : La commande SQL pour insérer une ligne dans la table `sales`. Les `%s` sont des placeholders pour les valeurs des colonnes.
- `sales` : La liste de tuples contenant les données à insérer dans la table.

En résumé, ce code crée une liste de tuples contenant les données des ventes et insère toutes ces données dans la table `sales` en une seule commande, en utilisant la méthode `executemany` pour optimiser les opérations d'insertion.


## Encapsulation d'opérations

```python
import psycopg2
import json

def insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, 
	discount):
	order_total = quantity * price
	if discount != 0:
		order_total = order_total * discount
	sale_data = {
	'order_num' : order_num,
	'cust_name' : cust_name,
	'prod_number' : prod_number,
	'prod_name' : prod_name,
	'quantity' : quantity,
	'price' : price,
	'discount' : discount,
	'order_total' : order_total
	}

	cur.execute('''INSERT INTO sales VALUES (%(order_num)s, 
		%(cust_name)s, %(prod_number)s, %(prod_name)s, %(quantity)s, 
		%(price)s, %(discount)s, %(order_total)s)''', sale_data)

if __name__ == "__main__":
   
   with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

   conn = psycopg2.connect(
	   database=config['db_name'],
	   user=config['db_user'],
	   password=config['db_password'],
	   host=config['db_host'],
	   port=config['db_port']
   )
   cursor = conn.cursor()
   print("Input sale data:\n")
   order_num = int(input("What is the order number?\n"))
   cust_name = input("What is the customer's name?\n")
   prod_number = input("What is the product number?\n")
   prod_name = input("What is the product name?\n")
   quantity = float(input("How many were bought?\n"))
   price = float(input("What is the price of the product?\n"))
   discount = float(input("What is the discount, if there is one?\n"))
   print("Inputting sale data:\n")
   insert_sale(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)
   conn.commit()
   conn.close()
```

Ce code est un script Python qui utilise la bibliothèque `psycopg2` pour interagir avec une base de données PostgreSQL. Il permet d'insérer des données de vente dans une table `sales` en fonction des entrées utilisateur. Voici une explication détaillée de chaque partie du code :

### Importations et Définition de la Fonction

```python
import psycopg2
import json
```

- **Importation des bibliothèques** : `psycopg2` est utilisé pour interagir avec PostgreSQL, et `json` est utilisé pour lire les configurations depuis un fichier JSON.

```python
def insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount
    sale_data = {
        'order_num': order_num,
        'cust_name': cust_name,
        'prod_number': prod_number,
        'prod_name': prod_name,
        'quantity': quantity,
        'price': price,
        'discount': discount,
        'order_total': order_total
    }

    cur.execute('''INSERT INTO sales VALUES (%(order_num)s, 
        %(cust_name)s, %(prod_number)s, %(prod_name)s, %(quantity)s, 
        %(price)s, %(discount)s, %(order_total)s)''', sale_data)
```

- **Fonction `insert_sale`** : Cette fonction prend plusieurs arguments correspondant aux colonnes de la table `sales` et un curseur de base de données `cur`.
  - **Calcul de `order_total`** : Le total de la commande est calculé en multipliant la quantité par le prix, puis en appliquant la remise si elle n'est pas nulle.
  - **Dictionnaire `sale_data`** : Les données de la vente sont stockées dans un dictionnaire.
  - **Exécution de la commande SQL** : La commande SQL `INSERT` est exécutée en utilisant les valeurs du dictionnaire `sale_data`.

### Bloc Principal

```python
if __name__ == "__main__":
    with open('3_postgresql/config.json', 'r') as f:
        config = json.load(f)
```

- **Lecture du fichier de configuration** : Le fichier `config.json` est ouvert et ses contenus sont chargés dans la variable `config`.

```python
    conn = psycopg2.connect(
        database=config['db_name'],
        user=config['db_user'],
        password=config['db_password'],
        host=config['db_host'],
        port=config['db_port']
    )
    cursor = conn.cursor()
```

- **Connexion à la base de données** : Une connexion à la base de données PostgreSQL est établie en utilisant les paramètres du fichier de configuration, et un curseur est créé.

```python
    print("Input sale data:\n")
    order_num = int(input("What is the order number?\n"))
    cust_name = input("What is the customer's name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = float(input("How many were bought?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount, if there is one?\n"))
```

- **Saisie des données de vente** : Les données de la vente sont demandées à l'utilisateur via des entrées interactives.

```python
    print("Inputting sale data:\n")
    insert_sale(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)
    conn.commit()
    conn.close()
```

- **Insertion des données de vente** : La fonction `insert_sale` est appelée avec les données de vente saisies. La transaction est ensuite validée avec `conn.commit()` et la connexion est fermée avec `conn.close()`.

### En résumé :

1. Le script lit les configurations de la base de données depuis un fichier JSON.
2. Il établit une connexion avec la base de données PostgreSQL.
3. Il demande à l'utilisateur de saisir les données de vente.
4. Il insère ces données dans la table `sales` de la base de données.
5. Il valide la transaction et ferme la connexion.


## Connection à une base de données PostgreSQL avec SQLAlchemy Core

```python
from sqlalchemy import create_engine
import json

# Lire le fichier de configuration
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

# Construire l'URL de connexion pour SQLAlchemy
db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

# Créer le moteur SQLAlchemy
engine = create_engine(db_url, echo=True)
```

Pour réécrire le code de connexion avec SQLAlchemy en utilisant les informations de configuration JSON de PostgreSQL, vous pouvez utiliser `create_engine` de SQLAlchemy de manière similaire à comment vous avez utilisé `psycopg2.connect`. Voici comment le faire :

1. Lire le fichier de configuration JSON.
2. Construire l'URL de connexion pour SQLAlchemy en utilisant les informations du fichier de configuration.
3. Créer le moteur SQLAlchemy avec cette URL de connexion.

Voici le code modifié :

```python
import json
from sqlalchemy import create_engine

# Lire le fichier de configuration
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

# Construire l'URL de connexion pour SQLAlchemy
db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

# Créer le moteur SQLAlchemy
engine = create_engine(db_url, echo=True)
```

### Explication :

1. **Lecture du fichier de configuration** :
    ```python
    with open('3_postgresql/config.json', 'r') as f:
        config = json.load(f)
    ```
    - Ouvre et lit le fichier de configuration JSON pour obtenir les détails de la base de données.

2. **Construction de l'URL de connexion** :
    ```python
    db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    ```
    - Construit l'URL de connexion en utilisant les informations du fichier de configuration. La chaîne de connexion est formatée pour PostgreSQL avec le driver `psycopg2`.

3. **Création du moteur SQLAlchemy** :
    ```python
    engine = create_engine(db_url, echo=True)
    ```
    - Crée un moteur SQLAlchemy avec l'URL de connexion générée. L'option `echo=True` permet de voir les requêtes SQL générées par SQLAlchemy pour le débogage.


## Opérations CRUD (Create, Read, Update, Delete) en utilisant SQLAlchemy Core pour interagir avec une base de données PostgreSQL
```python
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, select
import json

# Lire le fichier de configuration
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

# Construire l'URL de connexion pour SQLAlchemy
db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

# Créer le moteur SQLAlchemy
engine = create_engine(db_url, echo=True)

metadata = MetaData()


# sales_table = Table('sales', 
#       metadata,  
#       Column('order_num', Integer, primary_key=true),
#       Column('cust_name', String),
#       Column('prod_number', String),
#       Column('prod_name', String),
#       Column('quantity', Float),
#       Column('price', Float),
#       Column('discount', Float),
#       Column('order_total', Float))

sales_table = Table('sales', metadata, autoload_with=engine)

metadata.create_all(engine)

with engine.connect() as conn:

    # Read 
    for row in conn.execute(select(sales_table)):
        print(row)

    # Create
    insert_statement = sales_table.insert().values(
        order_num=1105910,
        cust_name='Syman Mapstone',
        prod_number='EB521',
        prod_name='Understanding Artificial Intelligence',
        quantity=3,
        price=19.5,
        discount=0,
        order_total=58.5
    )
    conn.execute(insert_statement)

    # Update
    update_statement = sales_table.update().where(sales_table.c.order_num == 1105910).values(quantity=2, order_total=39)
    conn.execute(update_statement)

    # Confirm Update
    reselect_statement = sales_table.select().where(sales_table.c.order_num == 1105910)
    updated_sale = conn.execute(reselect_statement).first()
    print(updated_sale)

    # Delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num == 1105910)
    conn.execute(delete_statement)

    # Confirm Delete
    not_found_set = conn.execute(reselect_statement)
    print(not_found_set.rowcount)

```

Bien sûr ! Voici une explication détaillée du script corrigé :

### Importation des modules et lecture du fichier de configuration
```python
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, select
import json

# Lire le fichier de configuration
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)
```
- **Importation des modules** :
  - `create_engine`, `Table`, `Column`, `Integer`, `Float`, `String`, `MetaData`, `select` sont importés depuis SQLAlchemy, une bibliothèque SQL pour Python.
  - `json` est importé pour lire les configurations de la base de données depuis un fichier JSON.

- **Lecture du fichier de configuration** :
  - Le fichier `config.json` est ouvert et son contenu est chargé dans la variable `config`.

### Création du moteur SQLAlchemy
```python
# Construire l'URL de connexion pour SQLAlchemy
db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

# Créer le moteur SQLAlchemy
engine = create_engine(db_url, echo=True)
```
- **Construction de l'URL de connexion** :
  - L'URL de connexion est construite en utilisant les informations de configuration pour se connecter à la base de données PostgreSQL.

- **Création du moteur SQLAlchemy** :
  - `create_engine` crée un moteur de connexion à la base de données. `echo=True` permet de voir les requêtes SQL générées par SQLAlchemy dans la console.

### Définition de la table `sales` et création du schéma
```python
metadata = MetaData()

sales_table = Table('sales', metadata, autoload_with=engine)

metadata.create_all(engine)
```
- **Création d'un objet `MetaData`** :
  - `MetaData` est un conteneur pour toutes les définitions de table et les informations sur les schémas.

- **Définition de la table `sales`** :
  - `Table` est utilisé pour définir la table `sales`. `autoload_with=engine` permet de charger la définition de la table à partir de la base de données existante.

- **Création du schéma** :
  - `metadata.create_all(engine)` crée toutes les tables définies dans `metadata`. Si les tables existent déjà, cette commande n'aura aucun effet.

### Connexion à la base de données et opérations CRUD
```python
with engine.connect() as conn:

    # Read 
    for row in conn.execute(select(sales_table)):
        print(row)

    # Create
    insert_statement = sales_table.insert().values(
        order_num=1105910,
        cust_name='Syman Mapstone',
        prod_number='EB521',
        prod_name='Understanding Artificial Intelligence',
        quantity=3,
        price=19.5,
        discount=0,
        order_total=58.5
    )
    conn.execute(insert_statement)

    # Update
    update_statement = sales_table.update().where(sales_table.c.order_num == 1105910).values(quantity=2, order_total=39)
    conn.execute(update_statement)

    # Confirm Update
    reselect_statement = sales_table.select().where(sales_table.c.order_num == 1105910)
    updated_sale = conn.execute(reselect_statement).first()
    print(updated_sale)

    # Delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num == 1105910)
    conn.execute(delete_statement)

    # Confirm Delete
    not_found_set = conn.execute(reselect_statement)
    print(not_found_set.rowcount)
```
- **Connexion à la base de données** :
  - `with engine.connect() as conn` crée une connexion contextuelle à la base de données.

- **Lecture des données (Read)** :
  - `select(sales_table)` sélectionne toutes les lignes de la table `sales` et les imprime.

- **Insertion d'une nouvelle ligne (Create)** :
  - `sales_table.insert().values(...)` crée une instruction d'insertion pour ajouter une nouvelle ligne à la table `sales`.
  - `conn.execute(insert_statement)` exécute cette instruction pour insérer la nouvelle ligne.

- **Mise à jour d'une ligne (Update)** :
  - `sales_table.update().where(sales_table.c.order_num == 1105910).values(quantity=2, order_total=39)` crée une instruction de mise à jour pour modifier la ligne où `order_num` est `1105910`.
  - `conn.execute(update_statement)` exécute cette instruction pour mettre à jour la ligne.

- **Confirmation de la mise à jour** :
  - `sales_table.select().where(sales_table.c.order_num == 1105910)` crée une instruction de sélection pour vérifier la mise à jour.
  - `updated_sale = conn.execute(reselect_statement).first()` exécute cette instruction et récupère la première ligne correspondante.

- **Suppression de la ligne (Delete)** :
  - `sales_table.delete().where(sales_table.c.order_num == 1105910)` crée une instruction de suppression pour supprimer la ligne où `order_num` est `1105910`.
  - `conn.execute(delete_statement)` exécute cette instruction pour supprimer la ligne.

- **Confirmation de la suppression** :
  - `conn.execute(reselect_statement)` exécute l'instruction de sélection pour vérifier si la ligne a été supprimée.
  - `print(not_found_set.rowcount)` imprime le nombre de lignes retournées par la sélection. Si `rowcount` est 0, cela signifie que la ligne a été supprimée avec succès.

Ce script montre comment effectuer des opérations CRUD (Create, Read, Update, Delete) en utilisant SQLAlchemy pour interagir avec une base de données PostgreSQL.


## Manipulation en utilisant SQLAlchemy ORM

```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import json

# Lire le fichier de configuration
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)

# Construire l'URL de connexion pour SQLAlchemy
db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

# Créer le moteur SQLAlchemy
engine = create_engine(db_url, echo=True)

# class Sale(Base):
#       __tablename__='sales',
#       Column('order_num', Integer, primary_key=true),
#       Column('cust_name', String),
#       Column('prod_number', String),
#       Column('prod_name', String),
#       Column('quantity', Float),
#       Column('price', Float),
#       Column('discount', Float),
#       Column('order_total', Float))

Base = automap_base()

Base.prepare(autoload_with=engine)

Sales = Base.classes.sales

with Session(engine) as session:

	# Read
	smallest_sale = session.execute(select(Sales).order_by(Sales.order_total)).scalar()
	print(smallest_sale.order_total)

	# Insert
	recent_sale = Sales(
            order_num=1105910, 
            cust_name='Syman Mapstone', 
            prod_number='EB521', 
            prod_name='Understanding Artificial Intelligence', 
            quantity=3, 
            price=19.5, 
            discount=0, 
            order_total=58.5
    )
	session.add(recent_sale)
	session.commit()

	# Update
	recent_sale.quantity = 2
	recent_sale.order_total = 39
	updated_sale = session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()
	print(updated_sale.quantity)
	print(updated_sale.order_total)
	session.commit()

	# Delete
	returned_sale = session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()
	session.delete(returned_sale)
	session.commit()
```


Ce script utilise SQLAlchemy pour interagir avec une base de données PostgreSQL. Il lit une configuration à partir d'un fichier JSON, établit une connexion à la base de données, puis effectue des opérations CRUD (Create, Read, Update, Delete) sur une table appelée `sales`. Voici une explication détaillée de chaque partie du script :

### Importation des modules et lecture du fichier de configuration
```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import json

# Lire le fichier de configuration
with open('3_postgresql/config.json', 'r') as f:
    config = json.load(f)
```
- **Importation des modules** :
  - `create_engine`, `select` sont importés depuis SQLAlchemy pour la création du moteur de base de données et les opérations de sélection.
  - `Session` est importé pour gérer les sessions de base de données.
  - `automap_base` est importé pour mapper automatiquement les classes aux tables existantes dans la base de données.
  - `json` est importé pour lire les configurations de la base de données depuis un fichier JSON.

- **Lecture du fichier de configuration** :
  - Le fichier `config.json` est ouvert et son contenu est chargé dans la variable `config`.

### Création du moteur SQLAlchemy
```python
# Construire l'URL de connexion pour SQLAlchemy
db_url = f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

# Créer le moteur SQLAlchemy
engine = create_engine(db_url, echo=True)
```
- **Construction de l'URL de connexion** :
  - L'URL de connexion est construite en utilisant les informations de configuration pour se connecter à la base de données PostgreSQL.

- **Création du moteur SQLAlchemy** :
  - `create_engine` crée un moteur de connexion à la base de données. `echo=True` permet de voir les requêtes SQL générées par SQLAlchemy dans la console.

### Définition des classes mappées automatiquement
```python
Base = automap_base()

Base.prepare(autoload_with=engine)

Sales = Base.classes.sales
```
- **Automap Base** :
  - `automap_base` est utilisé pour mapper automatiquement les tables de la base de données aux classes Python.

- **Préparation de la base** :
  - `Base.prepare(autoload_with=engine)` charge la structure de la base de données à partir du moteur, en mappant automatiquement les tables aux classes.

- **Accès à la classe `Sales`** :
  - `Sales = Base.classes.sales` donne accès à la classe mappée à la table `sales`.

### Opérations CRUD avec une session SQLAlchemy
```python
with Session(engine) as session:

    # Read
    smallest_sale = session.execute(select(Sales).order_by(Sales.order_total)).scalar()
    print(smallest_sale.order_total)

    # Insert
    recent_sale = Sales(
        order_num=1105910, 
        cust_name='Syman Mapstone', 
        prod_number='EB521', 
        prod_name='Understanding Artificial Intelligence', 
        quantity=3, 
        price=19.5, 
        discount=0, 
        order_total=58.5
    )
    session.add(recent_sale)
    session.commit()

    # Update
    recent_sale.quantity = 2
    recent_sale.order_total = 39
    updated_sale = session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()
    print(updated_sale.quantity)
    print(updated_sale.order_total)
    session.commit()

    # Delete
    returned_sale = session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()
    session.delete(returned_sale)
    session.commit()
```
- **Création d'une session** :
  - `with Session(engine) as session` crée une session contextuelle pour interagir avec la base de données.

- **Lecture des données (Read)** :
  - `session.execute(select(Sales).order_by(Sales.order_total)).scalar()` sélectionne la vente avec le plus petit `order_total` et l'imprime.

- **Insertion d'une nouvelle ligne (Create)** :
  - Un nouvel objet `Sales` est créé avec les valeurs spécifiées.
  - `session.add(recent_sale)` ajoute ce nouvel objet à la session.
  - `session.commit()` valide la transaction, insérant la nouvelle ligne dans la base de données.

- **Mise à jour d'une ligne (Update)** :
  - Les attributs `quantity` et `order_total` de `recent_sale` sont modifiés.
  - `session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()` vérifie la mise à jour.
  - `session.commit()` valide la transaction, mettant à jour la ligne dans la base de données.

- **Suppression de la ligne (Delete)** :
  - `session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()` sélectionne la ligne à supprimer.
  - `session.delete(returned_sale)` supprime cette ligne de la session.
  - `session.commit()` valide la transaction, supprimant la ligne de la base de données.

Ce script montre comment utiliser SQLAlchemy pour mapper automatiquement des tables de base de données existantes aux classes Python et comment effectuer des opérations CRUD en utilisant ces classes mappées.