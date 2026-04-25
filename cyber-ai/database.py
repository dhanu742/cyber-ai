import sqlite3
import bcrypt


# =========================
# CONNECT DATABASE
# =========================

def connect():

    return sqlite3.connect(
        "data.db",
        check_same_thread=False
    )


# =========================
# CREATE TABLES
# =========================

def create_tables():

    conn = connect()

    cur = conn.cursor()

    # users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password BLOB
    )
    """)

    # attacks table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS attacks (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data TEXT
    )
    """)

    # feedback table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data TEXT,

        prediction TEXT,

        feedback TEXT
    )
    """)

    conn.commit()

    conn.close()


# =========================
# REGISTER USER
# =========================

def register_user(username, password):

    conn = connect()

    cur = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:

        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


# =========================
# LOGIN USER
# =========================

def login_user(username, password):

    conn = connect()

    cur = conn.cursor()

    cur.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    user = cur.fetchone()

    conn.close()

    if user:

        stored_password = user[0]

        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):
            return True

    return False


# =========================
# INSERT ATTACK
# =========================

def insert_attack(data):

    conn = connect()

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO attacks (data) VALUES (?)",
        (data,)
    )

    conn.commit()

    conn.close()


# =========================
# GET ATTACKS
# =========================

def get_attacks():

    conn = connect()

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM attacks"
    )

    rows = cur.fetchall()

    conn.close()

    return rows


# =========================
# SAVE FEEDBACK
# =========================

def save_feedback(
    data,
    prediction,
    feedback
):

    conn = connect()

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO feedback
        (data, prediction, feedback)

        VALUES (?, ?, ?)
        """,

        (
            str(data),
            prediction,
            feedback
        )
    )

    conn.commit()

    conn.close()


# =========================
# INITIALIZE DATABASE
# =========================

create_tables()