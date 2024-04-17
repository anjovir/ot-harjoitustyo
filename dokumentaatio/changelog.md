## Viikko 3

- Luotu treeniohjelma-sivu, johon listataan ohjelmaan linkitetyt treenit
- Käyttäjä voi luoda treeniohjelmaan uuden treenin
- Treeniohjelmanäkymästä voidaan siirtyä tarkastelemaan yksittäistä treeniä ja sen liikkeitä
- Päivän treeniä (Workout of the day, WOD) voi muokata ja laajentaa
- Näihin rakennettu perusluokat:
    - services: wod_service, wprogram_service
    - repositories: wod_repository, wprogram_repository
    - entities: wod, workout_program
    - UI: edit_wod_view, new_wod_view, ui, wod_view, workout_view


## Viikko 4

- Käyttäjän luominen ja sisäänkirjautuminen
- Luotu luokat user.py, user_repository.py, user_service.py, create_user.py, login_view.py
- pohjana hyödynnetty kurssin esimerkkisovelluksen tehtävälistan sisäänkirjautumistoimintoa ja käyttäjähallintaa, jota muokattu sovellukseen sopivaksi
- muokattu lisäksi tiedostoja wprogram_service, wod_service, edit_wod_view, workout_view, ui, initialize_data

## Viikko 5
- käyttäjä voi poistaa päivän treenin omasta kuntosaliohjelmastaan
- muokattu mm. tiedostoja workout_view, wprogram_service, wprogram_repository
- luotu .env-muuttujat, joiden perusteella tietokannan sijainti määrittyy ja ohjelman voi alustaa komennolla invoke build