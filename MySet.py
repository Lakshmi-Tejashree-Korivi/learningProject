class MySet :
    def __init__(self,lst):
        hm1 = {}
        with open(L1, 'r') as f1:
                for line in f1:
                    hm[line] = None
        hm2 = {}
        with open(L2, 'r') as f2:
                for line in f2:
                    hm2[line]= None
    def union(self,L):
        for key,value in hm2.items():
                hm1[key]= None
        return hm1
    def intersection(self,L):
        for key in hm1:
            if key in hm2:
                    hm[key] = None
        return hm
    def minus (self,L):
        if L is L2:
            for key ,value in hm1.items():
                    if key not in hm2:
                        hm[key] = None
            return hm
        else :
            for key ,value in hm2.items():
                    if key not in hm1:
                        hm[key] = None
            return hm

    def __dump__(self,R):
        with open(R,'w') as outF:
            for line , one in h.items():
                outF.write(line+'\n')
    def __add__(self,L):
        return self.union(L)
    def __sub__(self,L):
        return self.minus(L)
    def __mod__(self,L):
        return self.intersection(L) 
