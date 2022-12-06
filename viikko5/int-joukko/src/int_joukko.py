KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.lukujoukko = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu_joukkoon(self, n):
        joukossa = False

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujoukko[i]:
                joukossa = True

        return joukossa

    def lisaa(self, n):
        if not self.kuuluu_joukkoon(n):
            self.lukujoukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm == len(self.lukujoukko):
                self.laajenna_taulukkoa()
            return True
        return False

    def poista(self, arvo):
        poistetun_sijainti = self.loyda_sijainti_ja_poista(arvo)

        if poistetun_sijainti != -1:
            self.muotoile_poisto(poistetun_sijainti)
            return True

        return False
    
    def loyda_sijainti_ja_poista(self,arvo):
        for paikka in range(0, self.alkioiden_lkm):
            if arvo == self.lukujoukko[paikka]:
                self.lukujoukko[paikka] = 0
                return paikka
        return -1

    def muotoile_poisto(self,sijainti):
        for paikka in range(sijainti, self.alkioiden_lkm):
            self.lukujoukko[paikka] = self.lukujoukko[paikka + 1]

        self.alkioiden_lkm = self.alkioiden_lkm - 1


    def laajenna_taulukkoa(self):
        taulukko_old = self.lukujoukko
        self.lukujoukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujoukko)

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def joukon_koko(self):
        return self.alkioiden_lkm

    def lukujoukko_lista(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujoukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.lukujoukko_lista()
        b_taulu = b.lukujoukko_lista()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.lukujoukko_lista()
        b_taulu = b.lukujoukko_lista()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.lukujoukko_lista()
        b_taulu = b.lukujoukko_lista()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujoukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujoukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujoukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
