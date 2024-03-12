import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.kortti2 = Maksukortti(100)
        self.kortti3 = Maksukortti(400)
    
    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassan_rahamaara_on_oikea_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_myytyjen_lounaiden_maara_on_oikea_alussa_m(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassan_myytyjen_lounaiden_maara_on_oikea_alussa_e(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_lounaan_ostaminen_kateisella_onnistuu(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(takaisin, 260)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisen_lounaan_ostaminen_kateisella_ei_onnistu(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(takaisin, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_lounaan_ostaminen_kateisella_onnistuu(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(takaisin, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaan_lounaan_ostaminen_kateisella_ei_onnistu(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(takaisin, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_ostaminen_kortilla_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kortti.saldo_euroina(), 7.60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    
    def test_maukkaan_lounaan_ostaminen_kortilla_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_lounaan_ostaminen_kortilla_ei_onnistu(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti2))
        self.assertEqual(self.kortti2.saldo_euroina(), 1.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_lounaan_ostaminen_kortilla_ei_onnistu(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti2))
        self.assertEqual(self.kortti2.saldo_euroina(), 1.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahan_lataaminen_kortille_onnistuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.kortti.saldo_euroina(), 20)
    
    def test_rahan_lataaminen_kortille_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
    
    def test_syo_maukkaasti_tasarahalla_kortilla(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti3))
        self.assertEqual(self.kortti3.saldo_euroina(), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    