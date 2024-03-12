import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortin_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

    def test_saldon_vahentaminen_toimii(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)
    
    def test_rahan_ottaminen_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahat_riittivat_bool_testi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(100))
        self.assertFalse(self.maksukortti.ota_rahaa(1500))