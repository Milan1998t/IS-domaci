import copy
import json
import numpy as np

from ispit import Ispit
from sala import Sala

brTesta = "6"

all_departments = []
ogranicenjeOdseciGodine = {}

with open("testovi/rok"+brTesta+".json", "rb") as read_file:
    rokoviJSON = json.load(read_file)


with open("testovi/sale"+brTesta+".json", "rb") as read_file:
    saleJSON = json.load(read_file)

print(rokoviJSON)

def formirajIspite(rokoviJSON):
    ispiti = []
    for rokJSON in rokoviJSON['ispiti']:
        odseci = []
        for odsek in rokJSON['odseci']:
            odseci.append(odsek)
            ogranicenjeOdseciGodine[odsek] = np.zeros(rokoviJSON["trajanje_u_danima"])
        ispiti.append(Ispit(rokJSON['sifra'],
                          rokJSON['prijavljeni'],
                          rokJSON['racunari'],
                          odseci))

    return ispiti

def formirajSale(saleJSON, dani):
    sale = []
    for d in range(dani):
        for t in range(1, 4+1):
            for salaJSON in saleJSON:
                sale.append(Sala(salaJSON['naziv'],
                              salaJSON['kapacitet'],
                              salaJSON['racunari'],
                              salaJSON['dezurni'],
                              salaJSON['etf'],
                              vreme = t,
                              dan = d + 1))
    return sale
ispiti = formirajIspite(rokoviJSON)

dani = rokoviJSON["trajanje_u_danima"]
print(ogranicenjeOdseciGodine)

def formirajDomene(ispiti, sale):
    domeni = {}
    for ispit in ispiti:
        domeni[ispit.sifraIspita] = copy.deepcopy(sale)
    return domeni


sale = formirajSale(saleJSON, dani)
domeni = formirajDomene(ispiti, sale)
