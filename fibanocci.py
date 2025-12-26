lst=[0,1]
def find(a,b,n):
    if(len(lst)!=n+1):

        b=a+b
        lst.append(b)
        print(lst)

        find(b-a,b,n)

find(0,1,4)
print(lst[-1])