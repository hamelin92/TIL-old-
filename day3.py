def prime_dict(a):
    b=0
    prime_list={1:2}
    ky=2
    if a==1:
        result={}
    else:
        for d in range(3, int(a) + 1):
            for e in prime_list.values():
                if d % e == 0:
                    b = b + 1
                    break
            if b == 0:
                prime_list[ky] = d
                ky = ky + 1
            else:
                b = 0
        result=prime_list
    return result

x= prime_dict(1)
print(x)
print(len(x))
