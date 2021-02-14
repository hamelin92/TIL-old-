## 세 정수 중 최대값 구하기

print('세 정수의 최댓값을 구합니다.')
a=int(input('정수 a의 값을 입력하세요.:'))
b=int(input('정수 b의 값을 입력하세요.:'))
c=int(input('정수 c의 값을 입력하세요.:'))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
print(f'최댓값은 {maximum}입니다.')


## 이름 입력, 출력

print('이름을 입력하세요:', end='')
name=input()
print(f'안녕하세요? {name} 님.')
