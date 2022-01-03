import numpy as np
import math as mat
import random as rand

        
finalSolution = np.zeros((1,6));
RADIUS = 15
signals =              [2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01, 1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
                       3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02, -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
                       7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01, 2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
                       5.827732223753571e-01, 3.686942505423780e-01];

def optimizationFunction(points,x):
    i = 0;
    sumIt = 0
    while i < 20 :
        if mat.sqrt(pow(x[0],2) + pow(x[1],2)) > RADIUS or mat.sqrt(pow(x[2],2) + pow(x[3],2)) > RADIUS:
            sumIt = 100;
        else:
            sumIt = sumIt + pow((x[4]/mat.sqrt(pow((15 * mat.cos(2 * mat.pi * i/20) - x[0]),2)
                    + pow(( 15 * mat.sin(2 * mat.pi * i/20) - x[1]),2)) + x[5]/mat.sqrt(pow((15 * mat.cos(2 * mat.pi * i/20) - x[2]),2) 
                    + pow(( 15 * mat.sin(2 * mat.pi * i/20) - x[3]),2)) - points[i]),2);
        i = i + 1;
    return sumIt;

def mixRandom(low, high):
    res = 0;
    res = low + (high - low) * rand.random();
    return res;

def crossFunction(P, Q, R):
    for i in range(50):
        randomNum = rand.randint(0,5);
        for j in range(6):
            if 0.9 > rand.uniform(0,1) or randomNum == j:
                Q[i][j] = R[i][j];
            else:
                Q[i][j] = P[i][j];
    return Q;
                
def diferentiationFunction(x):
    finishInd = 50;
    arrayP = np.zeros((50,6));
    arrayQ = np.zeros((50,6));
    arrayR = np.zeros((50,6));
    solution = np.zeros((1,6));
    ind = 0;
    flag = True;
    
    while ind < finishInd:
        for j in range(6):
            arrayP[ind][j] = mixRandom(-15,15);
        ind = ind + 1;
        
    while flag:
        for i in range(50):
            curr = optimizationFunction(x, arrayP[i]);
            if (curr < 10 ** -14):
                finishInd = i;
                flag = False;
        if  finishInd != 50:
            solution = arrayP[finishInd];
            return solution;         
        else:
           for i in range(50):
               #Get 3 random unique indexs
            flag1 = False
            arrGen = []
            while(not flag1):
                flag1 = True
                arrGen = rand.sample(range(0, 50), 3)
                for j in range(3):
                    if (arrGen[j] == i):
                        flag1 = False
                        break
                arrayR[i] = arrayP[arrGen[0]] + 0.8*(arrayP[arrGen[1]] - arrayP[arrGen[2]])
            
                crossFunction(arrayP, arrayQ, arrayR);
               
                if (optimizationFunction(x,arrayP[i]) > optimizationFunction(x,arrayQ[i])):
                    arrayP[i] = arrayQ[i];

#main:
finalSolution = diferentiationFunction(signals);
print("[Xp1, Yp1, Xp2, Yp2, A1, A2] = ");
print(finalSolution);
print("Optimization function = ")
print(optimizationFunction(signals,finalSolution));