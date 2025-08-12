accounts = [[1,5],[7,3],[3,5]]
richest=0
for row in accounts:
    sum=0
    for value in row:
        sum+=value
    if(sum>richest):
        richest=sum
print(richest)