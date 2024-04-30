# Ohjelmistotekniikka harjoitustyö
Sovelluksessa voi luoda ja suunnitella kuntosaliohjelman kuntosalitreenaamisen tueksi.

- linkki dokumentaatioon: [dokumentaatio](https://github.com/anjovir/ot-harjoitustyo/tree/main/dokumentaatio)
- linkki vaatimusmäärittelyyn: [vaatimusmäärittely](https://github.com/anjovir/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- linkki changelog-tiedostoon: [changelog](dokumentaatio/changelog.md)
- linkki arkkitehtuurikuvauksiin: [architecture](dokumentaatio/arkkitehtuuri.md)
- linkki käyttöohjeeseen: [user manual](https://github.com/anjovir/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- linkki viimeisimpään julkaisuun [Viikon 6 julkaisu](https://github.com/anjovir/ot-harjoitustyo/releases/tag/v6.0.3)

## Sovelluksen käynnistäminen:
- Asenna ensin poetryn riippuvuudet komennolla poetry install
- Tämän jälkeen tulee ajaa komento poetry run invoke build
- tämän jälkeen voit käynnistää sovelluksen komennolla poetry run invoke start

## Testaus
- Voit ajaa testiraportin komennolla poetry run invoke coverage-report