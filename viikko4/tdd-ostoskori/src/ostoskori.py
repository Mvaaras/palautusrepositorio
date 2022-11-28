from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset_lista = []

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.ostokset_lista:
            maara += ostos.lukumaara()
        return maara

    def hinta(self):
        hinta = 0
        for tuote in self.ostokset_lista:
            hinta += tuote.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset_lista:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.ostokset_lista.append(Ostos(lisattava))
        return

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.ostokset_lista:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostokset_lista.remove(ostos)
                return

    def tyhjenna(self):
        self.ostokset_lista = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset_lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
