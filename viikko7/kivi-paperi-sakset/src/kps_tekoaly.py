class KPSTekoaly:
    def __init__(self, tekoaly):
        self.tekoaly = tekoaly

    def siirto(self, ekan_siirto):
        alyn_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {alyn_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return alyn_siirto

