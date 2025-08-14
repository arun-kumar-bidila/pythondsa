grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
result=[[0 for _ in range(len(grid)-2)] for _ in range(len(grid)-2)]
print(result)

for i in range(0,len(result)):
    for j in range(0,len(result[i])):
       localmax=[]
       for x in range(i,i+3):
           for y in range(j,j+3):
               localmax.append(grid[x][y])
       result[i][j]=max(localmax)
print(result)
        


