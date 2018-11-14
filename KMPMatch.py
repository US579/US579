def KMPMatch(T,P):
    n = len(T)
    m = len(P)
    F = failureFunction(P)
    i , j = 0 , 0
    while i < n:
        if T[i] == P[j]:
            if j == m-1:
                return i - j
            else:
                i = i + 1
                j = j + 1
        else:
            if j > 0:
                j = F[j-1]
            else:
                i = i + 1
    return -1

def failureFunction(P):
    m = len(P)
    F = dict()
    F[0] = 0
    i,j = 0,0
    while i < m:
        if P[i] == P[j]:
            F[i] = j+1
            i = i + 1
            j = j + 1
        elif j > 0:
            j = F[j-1]
        else:
            F[i] = 0
            i = i+1
    return F


T = 'abacaabaccabacabaabb'
P = 'abacab'
print(KMPMatch(T,P))





