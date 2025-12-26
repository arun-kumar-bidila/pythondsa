customers = "YYNY"
penalty=[]
lstcustomer=list(customers)
for i in range(len(customers)+1):
    npenalty=0
    ypenalty=0
    if i!=0:
        nnewcustomer=lstcustomer[:i]
        npenalty=nnewcustomer.count("N")
    if i!=len(customers):

        ynewcustomer=lstcustomer[i:]
        ypenalty=ynewcustomer.count("Y")
    finalpenalty=npenalty+ypenalty
    penalty.append(finalpenalty)
print(penalty)
print(penalty.index(min(penalty)))