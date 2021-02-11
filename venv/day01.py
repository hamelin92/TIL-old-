a=input("소수 판독 숫자 입력")
b=int(a)
d=1
if b%3==0:
    print("{0}은 합성수이고 3의 배수입니다.".format(a))
else:
    while d<b**(1/2):
        d=d+1
        if b%d == 0:
            print("{0}은 합성수이고 {1}의 배수입니다.".format(a,d))
            break
        if d>b**(1/2) and b%d!=0:
            print("{0}은 소수입니다.".format(a))
            break

