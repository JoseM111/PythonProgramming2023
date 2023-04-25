# file: db/db.py
# =============================================

import pickle
# =============================================

DB_FILENAME = "data/rooms.db"
# =============================================

def load_rooms_db() -> dict:
    try:
        with open(file = DB_FILENAME, mode = "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_rooms_db(db):
    with open(DB_FILENAME, "wb") as file:
        pickle.dump(db, file)

rooms_db = load_rooms_db()
# =============================================
