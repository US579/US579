#sorting algorithem


#################################################
#bubble sorting

L = [7,8,5,2,4,6,3]
length = len(L)
#time complexity O(n^2)
def bubble_sort(L,length):
    if length < 2:
        return L
    for i in range(length-1):
        print(L)
        for j in range(length-i-1):
            if L[j+1] < L[j]:
                L[j+1] ,L[j] = L[j],L[j+1]
    return L

#print(bubble_sort(L,length))

#################################################

#quick sorting
#time complexity O(nlog(n))
def Quick_sort1(L):
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
            
    return Quick_sort1(l) + [key] + Quick_sort1(r)

def Quick_sort2(L,l,r):
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
    Quick_sort2(L,low,l-1)
    Quick_sort2(L,r+1,high)
    return L[::-1]
        
    
#print(Quick_sorting2(L,0,len(L)-1))


#################################################

#selection sorting
#time complexity O(n^2)
def Selection_sort1(L):
    lis = []
    for i in range(len(L)):
        small = min(L)
        lis.append(L.pop(L.index(small)))
    return lis

def Selection_sort2(L):
    length = len(L)
    for index in range(length):
        for i in range(index,length):
            if L[index] > L[i]:
                L[i],L[index] = L[index],L[i]
    return L
                
#print(Selection_sort2(L))       

#################################################

#insert sort
#time complexity :
#平均和最坏情况下的时间复杂度都是O(n^2)，最好情况下都是O(n)
def insert_sort(L):
    length = len(L)
    for i in range(length):
        for j in range(i-1,-1,-1):
            if L[i] > L[j]:
                continue
            else:
                L[i] ,L[j] = L[j] , L[i]
                i -=1
    print L

#insert_sort(L)









        

    
    
        
    
    
