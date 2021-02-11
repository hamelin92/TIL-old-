a=input("입력한 수 이하의 소수를 모두 출력합니다")
b=0
c={1:2}
ky=2
for d in range(3,int(a)+1):
    for e in c.values():
        if d%e==0:
            b=b+1
            break
    if b==0:
        c[ky]=d
        ky=ky+1
    else:
        b=0

print(c)
print(len(c))

x=input("N번째 소수 (N은 {0}이하)".format(len(c)))
print(c[int(x)])