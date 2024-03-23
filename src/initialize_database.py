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
        drop table if exists wod;
        ''')
    
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username TEXT PRIMARY KEY,
            password TEXT
        );
    ''')

    cursor.execute('''
        create table workout_program (
            id INTEGER PRIMARY KEY,
            wprogram_name TEXT,
            wod_name TEXT,
            weekday TEXT
        );
    ''')

    cursor.execute('''
        create table wod (
            id INTEGER PRIMARY KEY,
            wprogram_id INTEGER,
            exercise TEXT,
            sets TEXT,
            reps TEXT,
            weights TEXT,
                   
            FOREIGN KEY (wprogram_id)
            REFERENCES workout_program (id)
                
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__=="__main__":
    initialize_database()