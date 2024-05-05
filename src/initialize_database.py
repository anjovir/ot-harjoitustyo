from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists users;
        ''')

    cursor.execute('''
        drop table if exists workout_program;
        ''')

    cursor.execute('''
        drop table if exists wod_id_table;
        ''')

    cursor.execute('''
        drop table if exists wod_exercises;
        ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            wprogram_id,
            
            FOREIGN KEY (wprogram_id)
            REFERENCES workout_program (id)
            ON DELETE CASCADE
                   
        );
    ''')

    cursor.execute('''
        create table workout_program (
            id INTEGER PRIMARY KEY,
            wprogram_name TEXT
        );
    ''')

    cursor.execute('''
        create table wod_exercises (
            id INTEGER PRIMARY KEY,
            wod_id INTEGER,
            exercise TEXT,
            sets TEXT,
            reps TEXT,
            weights TEXT,
                   
            FOREIGN KEY (wod_id)
            REFERENCES wod_id_table (id)
            ON DELETE CASCADE
                
        );
    ''')

    cursor.execute('''
        create table wod_id_table (
            id INTEGER PRIMARY KEY,
            wprogram_id INTEGER,
            wod_name TEXT,
                   
            FOREIGN KEY (wprogram_id)
            REFERENCES workout_program (id)
            ON DELETE CASCADE
                
        );
    ''')

    connection.commit()


def create_test_db(connection):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO workout_program (wprogram_name) VALUES ('Test workout program')"
    )

    cursor.execute("""INSERT INTO wod_id_table (wprogram_id, wod_name)
                   VALUES (1, 'Test wod')""")

    cursor.execute("""INSERT INTO wod_exercises (wod_id,exercise, sets, reps, weights)
                VALUES (1, 'Testipenkki', 3, 10, 70)""")

    cursor.execute("""INSERT INTO users (username, password, wprogram_id)
                   VALUES ('Pekka', 'pekka1', 1)""")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


def initialize_test_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    create_test_db(connection)

    connection.commit()


if __name__ == "__main__":
    initialize_database()
