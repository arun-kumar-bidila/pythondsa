n=int(input("Enter a number:"))
num=n
nod=len(str(n))
print(nod)
total=0
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10
if(total==n):
    print("armstrong")
else:
    print("not")

