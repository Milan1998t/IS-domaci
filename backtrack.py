from podesavanja import ispiti
from podesavanja import sale
from podesavanja import domeni
from podesavanja import ogranicenjeOdseciGodine
import copy
import numpy as np
from podesavanja import dani

sum = 0;

#preimenovati sve val == sala
ogr = ogranicenjeOdseciGodine

def backtrackPretraga(vars, domains, solution, lvl, constraints, sum, ogr):
    if lvl == len(vars):
        return True
    v = vars[lvl]
    if v.sifraIspita not in solution:
        solution[v.sifraIspita] = []
    for val in domains[v.sifraIspita]:
        if isConsistentAssignment(v, val, vars, domains, constraints,ogr):
            solution[v.sifraIspita].append(val)
            flag = False;
            for t in solution[v.sifraIspita]:
                if t.vreme != val.vreme or t.dan != val.dan:
                    flag = True   
            if flag == True:
                solution[v.sifraIspita].remove(val)
                continue
            new_dom = copy.deepcopy(domains)
            #Ovo ispod je forwardChecking
            flag = False;
            for key,dom in new_dom.items():
                new_dom[key] = [x for x in new_dom[key] if x.ime != val.ime or x.dan != val.dan or x.vreme != val.vreme]
                if len(new_dom[key]) == 0:
                    flag = True;
            if flag:
                solution[v.sifraIspita].remove(val)
                continue
            kopija = copy.deepcopy(ogr)
            sum += val.kapacitet;
            
            newLvl = lvl
            if(sum >= v.brojPrijavljenih):
                for odsek in v.odseci:
                    kljuc = odsek + str(v.godinaStudija)
                    if(kljuc not in kopija):
                        kopija[kljuc] = np.zeros(dani)
                        
                    kopija[odsek + str(v.godinaStudija)][val.dan - 1] = 1
                new_dom[v.sifraIspita] = copy.deepcopy(solution[v.sifraIspita])
                sum = 0
                newLvl += 1
            if backtrackPretraga(vars, new_dom, solution, newLvl, constraints, sum, kopija):
                return True
            
            sum -= val.kapacitet
            solution[v.sifraIspita].remove(val)
    return False


def isConsistentAssignment(v, val, vars, domains, constraints, ogr):
    for odsek in v.odseci:
        kljuc = odsek + str(v.godinaStudija)
        if(kljuc in ogr and ogr[kljuc][val.dan-1] == 1):
            return False
    if not val.imaKomp and v.potrebnoKomp:
        return False
    return True

resenje = {}
suma = 0
backtrackPretraga(ispiti, domeni, resenje, 0, [], 0, ogr)
for k,v in resenje.items():
    print(k)
    for soba in v:
        soba.print()
        suma += soba.brojDezurnih;
        if(soba.naEtfu == 0):
            suma += 1.2;
print (suma)