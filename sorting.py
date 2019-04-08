#sorting algorithem

#bubble sorting

L = [3,5,15,2,32,12,43,23,1,5,6,3,435,43,21]
length = len(L)
#time complexity O(n^2)
def bubble_sorting(L,length):
    if length < 2:
        return L
    for i in range(length-1):
        for j in range(length-i-1):
            if L[j+1] < L[j]:
                L[j+1] ,L[j] = L[j],L[j+1]
    return L

#print(bubble_sorting(L,length))
        
    
    
def Quick_sorting1(L):
    if len(L) <= 1:
        return L
    l = []
    r = []
    key = L.pop(0)
    for i in L:
        if i < key :
             l.append(i)
        
        else:
            r.append(i)
    return quick_sorting(l) + [key] + quick_sorting(r)

def Quick_sorting2(L,l,r):
    if l>r:
        return L
    key = L[l]
    low = l
    high = r
    while l < r:
        while l<r and key >= L[r]:
            r -=1
        L[l] = L[r]
        while l<r and key < L[l]:
            l += 1
        L[r] = L[l]
    L[l] = key
    Quick_sorting2(L,low,l-1)
    Quick_sorting2(L,r+1,high)
    return L[::-1]
        
    
print(Quick_sorting2(L,0,len(L)-1))

    
    
        
    
    
