# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="toDo"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT, task_status TEXT, task_due_date DATE)')


def add_data(task, task_status, task_due_date):
    c.execute('INSERT INTO taskstable(task, task_status, task_due_date) VALUES (%s,%s,%s)',
              (task, task_status, task_due_date))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM taskstable')
    data = c.fetchall()
    return data


def view_only_tasks():
    c.execute('SELECT task FROM taskstable')
    data = c.fetchall()
    return data


def get_task(task):
    c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
    data = c.fetchall()
    return data


def edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date):
    c.execute("UPDATE taskstable SET task=%s, task_status=%s, task_due_date=%s WHERE task=%s and task_status=%s and "
              "task_due_date=%s", (new_task, new_task_status, new_task_due_date, task, task_status, task_due_date))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(task):
    c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
    mydb.commit()
