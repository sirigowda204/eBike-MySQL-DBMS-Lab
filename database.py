import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT, task_status TEXT, task_due_date DATE)')


def add_data(task, task_status, task_due_date):
    c.execute('INSERT INTO taskstable(task, task_status, task_due_date) VALUES (?,?,?)',
              (task, task_status, task_due_date))
    conn.commit()


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
    c.execute("UPDATE taskstable SET task=?, task_status=?, task_due_date=? WHERE task=? and task_status=? and "
              "task_due_date=?", (new_task, new_task_status, new_task_due_date, task, task_status, task_due_date))
    conn.commit()
    data = c.fetchall()
    return data


def delete_data(task):
    c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
    conn.commit()