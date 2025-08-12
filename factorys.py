from math import sqrt
n=36
result=[]
for i in range(1,int(sqrt(n)+1)):
        if(n%i==0):
            result.append(i)
            if(n//i!=i):
               result.append(n//i)
print(result)
               
        
