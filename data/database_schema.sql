CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT
        );

CREATE TABLE workout_program (
            id INTEGER PRIMARY KEY,
            wprogram_name TEXT,
            wod_name TEXT,
            weekday TEXT
        );
        
CREATE TABLE wod (
            id INTEGER PRIMARY KEY,
            wprogram_id INTEGER,
            wod_name TEXT,
            exercise TEXT,
            sets TEXT,
            reps TEXT,
            weights TEXT,
                   
            FOREIGN KEY (wprogram_id)
            REFERENCES workout_program (id)
                
        );
