# Chapter03-4
# 파이썬 tuple
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x)    # 불변 : 기준값, 사람의 정보

#선언
#b = (1)                     #원소가 1개이면 int 형
#print(type(a), type(b))
a = ()
b = (1,)                    # ,를 찍어주면 tuple형
#print(type(a), type(b))
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))           # 튜플을 list형태로 형변환 (한글자 by 한글자) -> 불변의 성질이 없어짐

# 수정 x
#d[0] = 1500

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>>')
print('c + d', c + d)       # 내부의 원소의 변경은 안되지만, 연산은 허용
print('c * 3 - ', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))           # 3이 index 어디에 있나
print('a - ', a.count(2))
print()

# 팩킹 & 언팩킹 (Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')        # 4개의 원소를 하나로 묶음(인덱싱이 이루어짐)

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t        # Unpacking : 하나로 되었던 튜플을 각각 변수로 할당

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

t2 = 1, 2, 3        # 괄호는 생략가능 - 전부 tuple
t2 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
