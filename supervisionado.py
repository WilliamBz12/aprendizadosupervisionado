
amostras = []

with open ('haberman.data') as f:
    for linha in f.readlines():
        atri = linha.replace('\n', '').split(',')
        amostras.append([int(atri[0]), int(atri[1]), int(atri[2]), int(atri[3])])

def infodata(amostras, verbose=True):
    if verbose:
        print('Total de amostras: %d' % len(amostras))
    rotulo1, rotulo2 = 0, 0
    for amostra in amostras:
        if amostra[-1] == 1:
            rotulo1 += 1
        else :
            rotulo2 += 1
    if verbose: 
        print('1: %d' %rotulo1)
        print('2: %d' %rotulo2)
    return [len(amostras), rotulo1, rotulo2]

p = 0.6
_, rot1, rot2 = infodata(amostras, False)

treinamento, teste = [], []
maxrot1, maxrot2 = rot1*p, p*rot2
to1, to2 = 0, 0
for amostra in amostras:
  
    if(to1 + to2) < (maxrot1+maxrot2):
        
        treinamento.append(amostra)
        
        if amostra[-1] == 1 and to1 < maxrot1:
            to1 += 1
        else:
            to2 += 1
    else :
        teste.append(amostra)
import math

def dist_euclidiana (v1, v2) :
    dim, soma = len(v1), 0
    for i in range(dim-1):
        soma += math.pow(v1[i]-v2[i], 2)
    return math.sqrt(soma)


def knn(dbtreinamento, novaamostra, K):
    dist, tam_treinamento = {} , len(dbtreinamento)

    for i in range(tam_treinamento):
        d = dist_euclidiana(dbtreinamento[i], novaamostra)
        dist[i] = d
      
    k_vizinhos = sorted (dist, key=dist.get)[:K]
    
  
    qtd1, qtd2 = 0, 0
    for ind in k_vizinhos:
        if(dbtreinamento[ind][-1] == 1):
            qtd1 += 1
        else:
            qtd2 += 1
            
    if qtd1 > qtd2:
        return 1;
    else:
        return 2;

print("Resultado da amostra 80: ")
print(knn(treinamento, teste[80], 21))
