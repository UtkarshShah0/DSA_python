#Q7 Rotate matrix by 90

def rot(A):
    n=len(A[0])

    for i in range(n//2):
        for j in range(i, n - i - 1):
            temp = A[i][j]
            print("A[i][j]",i," ",j)
            A[i][j] = A[n-1-j][i]
            print("A[n-1-j][i]",n-1-j," ",i)
            A[n-1-j][i] = A[n-1-i][n-1-j]
            print("A[n-1-i][n-1-j]",n-1-i," ",n-1-j)
            A[n-1-i][n-1-j] = A[j][n-1-i]
            print("A[j][n-1-i]",j," ",n-1-i)
            print("Loop Completed")
            print("  ")
            A[j][n-1-i] = temp
def toprin(A):
    n=len(A[0])
    for i in range(n):
        print(A[i])

a=[[1,2,3],[4,5,6],[7,8,9]]
rot(a)
toprin(a)
            
            
