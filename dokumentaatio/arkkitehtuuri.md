Ohjelma perustuu kerrosarkkitehtuurin seuraavan pakkauskaavion mukaisesti:

![Pakkauskaavio](./kuvat/Pakkauskaavio.png)

Sovelluksen loogisen tietomallin muodostavat luokat User, Wod ja Workout_program:

```mermaid
---
Workout program
---
 classDiagram
    User "1" -- "*" Workout_program
    Workout_program "1" -- "*" Wod
    class User{
        username
        password
    }
    class Workout_program{
        wp_id
        wprogram_name
        wod_name
        wod_id
        

    }
    class Wod{
        id
        wod_name
        exercise
        sets
        reps
        weights
    }

    
```

Toiminnallisista kokonaisuuksista vastaavat luokat user_service, wod_service ja wprogram_service. Näissä on rakennettu käyttöliittymän toiminnoille omat metodit, esim. 
- login(username, password)
- save_new_wod(entries)
- initialize_wp_view()

