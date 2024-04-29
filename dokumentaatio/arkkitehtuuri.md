# Arkkitehtuuri

## Rakenne

Ohjelma perustuu kerrosarkkitehtuurin seuraavan pakkauskaavion mukaisesti:

![Pakkauskaavio](./kuvat/Pakkauskaavio.png)

Pakkaus ui sisältää käyttöliittymän, services sovelluslogiikan ja repositories tietojen pysyväistallennuksen koodin. Entities sisältää luokkia, jotka ilmentävät sovelluksen käyttämiä tietokohteita.

## Sovelluslogiikka

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

UserService pääsee käsiksi käyttäjiin tietojen tallennuksesta vastaavan luokan kautta, joka sijaitsee repositories pakkauksen luokassa UserRepository. Vastaavasti Wprogram service pääsee käsiksi saman pakkauksen WorkoutProgramRepositoryn kautta kyseisen luokan dataan ja vastaava repository löytyy myös palvelulle WodService.

## Tietojen pysyväistallennus

Pakkaus `repositories` sisältää luokat UserRepository, WorkoutProgramRepository ja WodRepository, joiden avulla tiedot voidaan tallentaa SQLite-tietokantaan.
Luokat noudattavat Repository-suunnittelumallia ja ne on mahdollista korvata vaihtoehtoisilla toteutuksilla tallennustavan vaihtuessa.

Sovelluksen juuresta löytyy .env-tiedosto, jossa on määritelty tiedostojen nimet.

Sovelluksen tiedot tallennetaan SQLiten tietokantaan, joka alustetaan initialize_database.py-tiedostossa.

## Keskeisiä toiminnallisuuksia

Alla on kuvattu osa sovelluksen toiminnallisuuksista.

### Käyttäjä kirjautuu sisälle kuntosaliohjelmaansa

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UserService
  participant UserRepository
  User->>UI: click "Login" button
  UI->>UserService: login("antti", "antti1")
  UserService->>UserRepository: find_by_username("antti")
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->UI: _show_workout_view()
```

### Käyttäjä tallentaa kuntosaliohjelmaan uuden treenin

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant WodService
  participant WodRepository
  participant UserService
  participant UserRepository
  participant WorkoutProgramRepository
  User->>UI: click "New WOD" button
  UI->>UI: _show_new_wod_view()
  User->>UI: Fill in workout name, exercise, sets, reps, weights
  User->>UI: click "Save" button
  UI->>WodService: save_new_wod(entries)
  WodService->>UserService: get_current_user()
  WodService->>WorkoutProgramRepository: find_wprogram_id_by_user("current_user")
  WodService-->>WodRepository: write(wod_name, wprogram_id, sets, reps, weights)
  UI->UI: _show_new_wod_view()
  ```