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