# Ohjelmistotekniikka harjoitustyö
Sovelluksessa voi luoda ja suunnitella kuntosaliohjelman kuntosalitreenaamisen tueksi.

- linkki käyttöohjeeseen: [user manual](https://github.com/anjovir/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- linkki vaatimusmäärittelyyn: [vaatimusmäärittely](https://github.com/anjovir/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- linkki arkkitehtuurikuvauksiin: [architecture](dokumentaatio/arkkitehtuuri.md)
- linkki changelog-tiedostoon: [changelog](dokumentaatio/changelog.md)
- linkki työaikakirjanpitoon: [työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)


## Sovelluksen käynnistäminen:
- Asenna ensin poetryn riippuvuudet komennolla poetry install
- Tämän jälkeen tulee ajaa komento poetry run invoke build
- tämän jälkeen voit käynnistää sovelluksen komennolla poetry run invoke start

## Testaus
- Testit voi ajaa komennolla poetry run invoke test
- Voit ajaa testikattavuusraportin komennolla poetry run invoke coverage-report

## Pylint
- Tarkistukset tiedoston .pylintrc määritelmien mukaan voi suorittaa komennolla poetry run invoke lint