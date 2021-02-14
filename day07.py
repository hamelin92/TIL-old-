import sys; sys.stdin = open("input.txt", "r")

N , M = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
C = [list(map(int, input().split())) for i in range(0,Q)]


B= []
D= []
for i in range(0,Q):
    for j in range(0,N):
        B=[(A[N-j-1]+C[i][0])%M]+B[:]
        D.append(B[:]+[0 for num in range(0,N)]+[N-j])
        D.sort()
    D.sort()
    print(D[C[i][1]-1][len(D[C[i][1]-1])-1])
    B=[]
    D=[]