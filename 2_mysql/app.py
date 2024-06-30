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


if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()

    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)
    
    db.close()