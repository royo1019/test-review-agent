import sqlite3

def get_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username='" + username + "'"
    user = cursor.execute(query).fetchone()

    if user and user[2] == password:
        return {"id": user[0], "username": user[1]}

    return None

def delete_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"DELETE FROM users WHERE username='{username}'"
    cursor.execute(query)
    conn.commit()
