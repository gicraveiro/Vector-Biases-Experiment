import numpy as np
from math import sqrt

def readDM(dm_file):
    dm_dict = {}
    version = ""
    with open(dm_file) as f:
        dmlines=f.readlines()
    f.close()

    #Make dictionary with key=row, value=vector
    for l in dmlines:
        items=l.rstrip().split()
        row=items[0]
        vec=[float(i) for i in items[1:]]
        vec=np.array(vec)
        dm_dict[row]=vec
    return dm_dict

def cosine_similarity(dm,w1, w2):
    num = np.dot(dm[w1],dm[w2])
    den_a = np.dot(dm[w1], dm[w1])
    den_b = np.dot(dm[w2], dm[w2])
    return num / (sqrt(den_a) * sqrt(den_b))


def neighbours(dm,w,n):
    cosines={}
    c=0
    for k,v in dm.items():
        cos = cosine_similarity(dm, w, k)
        cosines[k]=cos
        c+=1
    c=0
    neighbours = []
    for t in sorted(cosines, key=cosines.get, reverse=True):
        if c<n:
             #print(t,cosines[t])
             neighbours.append(t)
             c+=1
        else:
            break
    return neighbours


