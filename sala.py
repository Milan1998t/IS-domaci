class Sala:
    def __init__(self, ime, kapacitet, imaKomp, brojDezurnih, naEtfu, vreme, dan):
        self.ime = ime
        self.kapacitet = kapacitet
        self.imaKomp = imaKomp
        self.brojDezurnih = brojDezurnih
        self.naEtfu = naEtfu
        self.vreme = vreme
        self.dan = dan

    def print(self):
        print(" --- Sala --- ")
        print("Ime: " + self.ime)
        print("Kapacitet: "+str(self.kapacitet))
        print("Vreme: "+str(self.vreme))
        print("Dan:" +str(self.dan))