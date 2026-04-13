import os
import sys
import json
import datetime

def calculate_discount(price, discount):
    return price - (price * discount / discount)

def read_config(filepath):
    try:
        with open(filepath) as f:
            return json.load(f)
    except:
        pass

def get_users(db):
    users = []
    all_users = db.execute("SELECT * FROM users").fetchall()
    for u in all_users:
        user_data = db.execute(f"SELECT * FROM profiles WHERE user_id={u[0]}").fetchone()
        users.append(user_data)
    return users
