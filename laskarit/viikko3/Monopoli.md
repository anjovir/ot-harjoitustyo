```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Ruutu "3" -- "3" Sattuma
    Ruutu "3" -- "3" Yhteismaa
    Ruutu "2" -- "2" Laitokset
    Ruutu "4" -- "4" Asemat
    Ruutu "22" -- "22" Katu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "40" -- "40" Ruutu : toiminto
    Sattuma "10" -- "10" Sattumakortti
    Yhteismaa "10" -- "10" Yhteismaakortti
    Sattumakortti "1" -- "1" Sattumakortti : toiminto
    Yhteismaakortti "1" -- "1" Yhteismaakortti : toiminto
    Katu "1" -- "4" Talo
    Katu "1" -- "1" Hotelli
    Katu "1" -- "1" Pelaaja
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "1" Rahaa
```
