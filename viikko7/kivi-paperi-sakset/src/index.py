from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from ksp import KiviPaperiSakset as KSP


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = KSP(KPSPelaajaVsPelaaja())
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = KSP(KPSTekoaly(Tekoaly()))
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = KSP(KPSTekoaly(TekoalyParannettu(10)))
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
