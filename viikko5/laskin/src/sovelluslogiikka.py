class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    def miinus(self, arvo):
        self.aseta_arvo(self.tulos - arvo)

    def plus(self, arvo):
        self.aseta_arvo(self.tulos + arvo)

    def nollaa(self):
        self.aseta_arvo(0)

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo

    def kumoa(self):
        self.aseta_arvo(self.edellinen)
