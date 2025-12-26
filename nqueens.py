ans=[]
count=0
board=[]
board=["...."]*4
print(board)
n=4

def isSafe(board,row,col,n):
    for i in range(n):
        if(board[row][i]=="Q"):
             return False
    for j in range(n):
        if(board[j][col]=="Q"):
             return False
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]=="Q":
            return False
        i-=1
        j-=1
    i=row
    j=col
    while i>=0 and j<n:
        if board[i][j]=="Q":
            return False
        i-=1
        j+=1
    return True


def findqueens(board,row,n):
    global count
    if(row==n):
        ans.append(board[:])
        count+=1
        return
    for j in range(n):
        if(isSafe(board,row,j,n)):
            rowlist=list(board[row])
            rowlist[j]="Q"
            board[row]="".join(rowlist)

            findqueens(board,row+1,n)
            rowlist[j]="."
            board[row]="".join(rowlist)
        
findqueens(board,0,n)
print(ans)
print(count)
        
    


    
