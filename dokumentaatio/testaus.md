# Testausdokumentti

Ohjelmaa on testattu yksikkö- ja integraatiotestein automatisoidusti, jonka lisäksi sitä on testattu myös manuaalisesti.

## Yksikkö- ja integraatiotestaus

Sovelluslogiikasta vastaavat kolme luokkaa wprogram_service, wod_service ja user_service. Näitä on testattu testiluokilla TestWprogramService ja TestWodService, mutta UserService luokkaa ei ole suoraan testattu yksikkötestein. Näiden testit alustetaan kutsumalla initialize_databasen initialize_test_db-metodia, joka luo tietokantaan testikäyttäjän ja testiohjelman. Näiden pohjalta tarkistetaan, toimivatko testit.

## Repositoriot

Luokkkia user_repository, wod_repository ja wprogram_repository testataan vastaavilla testiluokilla TestUserRepository, TestWodRepository ja TestWprogramRepository.

## Testauskattavuus

Käyttöliittymää ei ole testattu, mutta testauksen haaraumakattavuus on tällä hetkellä 74%. Eniten testaamatta on jäänyt esim. UserService.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti.

### Asennus ja alkuvaiheen konfigurointi

Sovellus on haettu ja testattu käyttöohjeen kuvaamalla tavalla Linux-ympäristössä.

Sovellusta on testattu sekä alkuvaiheen tilanteessa, jossa käyttäjä luo ensimmäinen uuden harjoitusohjelman, että tilanteessa, jos vanhaa dataa jo löytyyy.

### Toiminnallisuudet

Kaikki määrittelydokumentin ja käyttöohjeen toiminnallisuudet on käyty läpi erilaisilla syötteillä.

## Jäjelle jääneitä laatuongelmia

Testitietokannan luonti ei testien aikana onnistu lukuisista yrityksistä huolimatta vaan testauksessa hyödynnetään tuotantotietokantaa, jolloin siihen aiemmin tallennetut tiedot poistetaan jokaisen testiajon yhteydessä.