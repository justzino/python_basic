# Chapter03-3
# 파이썬 list
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []          #빈 list
b = list()      #빈 list
c = [70, 75, 80, 85]        # 0 1 2 3 / len(c) -> 4
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1], e[2])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))           # 문자열을 list형태로 형변환 (한글자 by 한글자)

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))       #같은 자료형끼리만 + 긴,ㅇ

# 값 비교
print(c == c[:3] + c[3:])       # 동일 = true

# 같은 id 값
temp = c
print(id(temp))
print(id(c))            # 파일성의 효율성때문에 같은 주소값 공유
print(c == temp)


# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']        # list원소로 str 3개가이 들어감
print('c - ', c)
c[1:2] = [['a', 'b', 'c']]      # c[1]의 자리에 ['a', 'b', 'c'] list가 들어감
print('c - ', c)
c[1] = ['a', 'b', 'c']          # c[1]의 자리에 ['a', 'b', 'c'] list가 들어감 / c[1:2]과 다름을 주의!!!
print('c - ', c)
c[1:3] = []                     # c[1],c[2] 삭제됨 but, 이렇게 지우지는 않음
print('c - ', c)
del c[3]                        # c[3]삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)                 # .append : a의 마지막에 추가
print('a - ', a)
a.sort()                    # 오름차순으로 정렬
print('a - ', a)
a.reverse()                 # 들어있는 data를 역순으로 정렬
print('a - ', a)
print('a - ', a.index(5), a[5])     # index 가져오는 법 둘다 가능
a.insert(2, 3)              # .insert(2,3) : a[2] 에 3을 추가
print('a - ', a)
a.remove(3)                 # .remove : 해당값을 제거(앞에서부터 찾는듯..)
print('a - ', a)
print('a - ', a.pop())      #마지막 index를 pop (lifo)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))   # .count (4) : 4의 개수가 몇개?
ex = [8, 9]
a.append(ex)
print('a - ', a)
a.extend(ex)
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(2 is data)
