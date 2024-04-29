# Käyttöohje

Lataa projektin viimeisin julkaisu: [release](https://github.com/anjovir/ot-harjoitustyo/releases). Voit valita lähdekoodin Assets osion alta.

## Konfigurointi

Tiedostojen tallenukseen käytettävien tiedostojen nimiä voi muokata käynnistyhakemiston tiedoston .env kautta. Tiedosto luodaan automaattisesti *data*-hakemistoon, mikäli näitä ei siellä aiemmin ole luotu muodossa:

DATABASE_FILENAME=database.sqlite

## Ohjelman käynnistäminen

Ennen sovelluksen käynnistämistä asenna riippuvuudet komennolla:

`poetry install`

Tämän jälkeen suorita alustus komennolla:

`poetry run invoke build`

Jonka jälkeen voit käynnistää ohjelman komennolla:

`poetry run invoke start`

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään, johon voi kirjoittaa käyttäjätunnuksen ja salasanan sekä painamalla "Login"-painiketta.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä voidaan siirtyä uuden käyttäjän luomisen näkymään painamalla nappia "Create user". Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Create"-nappia.

Tämän jälkeen voidaan palata kirjautumisnäkymään painamalla "Back to login" -nappia.

## Uuden päivän treenin luominen

Käyttäjä pääsee tämän jälkeen listanäkymään, jossa näkyy oman kuntosaliohjelman treenilistaus.

Mikäli yhtään treeniä ei ole tehtynä, käyttäjä voi luoda sellaisen painamalla nappia "Create WOD".

Tämän jälkeen käyttäjä siirtyy päivän treenin näkymään "WOD-view", jossa käyttäjä voi nimetä treenikokonaisuuden ja kirjata treenin nimen, sarjat, toistot ja painot. Kaikki treenien kirjaukset ovat tekstityyppisiä, joten painoksi voi ilmoittaa myös esim. oman kehon painon - tai jättää tyhjäksi.

Tämän jälkeen käyttäjä voi tallentaa treenin ja palata kuntosaliohjelmanäkymään, jonka kautta voi luoda uuden treenin ja suunnittelemaan siten koko viikon treeniohjelman.

Käyttäjä voi myös tästä näkymästä poistaa yksittäisen treenin tai kaikki treenit tai jopa poistaa omat käyttäjätietonsa ja siihen liittyvät treenit tietokannasta.

Klikkaamalla lopuksi "Logout", käyttäjä voi kirjautua näkymästä ulos.
