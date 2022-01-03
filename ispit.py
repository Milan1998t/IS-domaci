class Ispit:
    def __init__(self, sifraIspita, brojPrijavljenih, potrebnoKomp, odseci):
        self.sifraIspita = sifraIspita
        self.brojPrijavljenih = brojPrijavljenih
        self.potrebnoKomp = potrebnoKomp
        self.odseci = odseci
        self.godinaStudija = self.sifraIspita[5]