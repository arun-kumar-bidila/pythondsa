n=1213
num=n
result=0
while(num>0):
    ld=num%10
    result=result*10+ld
    num=num//10
if(result==n):
    print("true")
else:
    print("false")

    
