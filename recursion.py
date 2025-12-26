# frds=list(range(1,n+1))
frds=[1,2,3,4,5]
k=2
def findlost(frds,idx):
    i=idx
    kval=k
    while True:
        kval-=1
        if(kval==0):
            del frds[i]
            if(len(frds)!=1):
                return findlost(frds,i)
            else:
                return frds[0]
        i=(i+1)% len(frds)
print(findlost(frds,0))