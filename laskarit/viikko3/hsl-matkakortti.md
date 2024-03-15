sequenceDiagram
   participant L as laitehallinto
   participant R as rautatietori
   participant R6 as ratikka6
   participant B as bussi244
   participant Li as lippu_luukku
   main->>L: lisaa_lataaja(R)
   main->>L: lisaa_lukija(R6)
   main->>L: lisaa_lukija(B)
   main->>Li: osta_matkakortti("Kalle")
   Li->>+kallen_kortti: uusikortti
   main->>R: lataaarvoa(kallen_kortti, 3)
   R-->>-kallen_kortti: 3
   main->>+R6: ostalippu(kallen_kortti, 0)
   R6->>+kallen_kortti: 1.5
   kallenkortti-->>-R6: vahenna_arvoa(1,5)
   main->>B: ostalippu(kallenkortti,2)
   B->>kallen_kortti: 3.5
   kallen_kortti-->>B: vahennaarvoa(3.5)
