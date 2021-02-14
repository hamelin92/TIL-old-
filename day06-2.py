##import sys; sys.stdin = open("input.txt", "r")
win = 39/80
lose = 1-win
a1=[win, 0]
a2=[0, lose]

a=[a1,a2]
a
print(a)


arr=[[1,2,3], [4,5,6], [7,8,9]]
print(arr)
x=int(input("1~9 숫자"))
var=0
for j in range(0,len(arr)):
    for k in range(0,len(arr[j])):
        if x==arr[j][k]:
            print(f'{x}는 {j+1}행 {k+1}열에 존재')
            var=var+1
            break
        elif j +1 == len(arr) and k+1 == len(arr[j]):
            print("결과가 없습니다")
            var=var+1
            break
    if var > 0:
        break
A=[]
B=[]
C=[]
D=[]
N=int(input())
M=int(input())
for i in range(0, N):
    A.append(int(input()))
print(A)
Q=int(input())
for i in range(0,Q):
    C.append([int(input()), int(input())])
    print(C[i])
for i in range(0,Q):
    for j in range(0,N):
        B.append((A[j]+C[i][0])%M)
        D=D+[B[:]]
        print(B)
        print(D)
    D.sort()
    print(D[C[i][1]-1])
    B=[]
    D=[]
