# Chapter03-5
# 파이썬 dictionary
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언 : {key : value}
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([                     # list -> dict 형변환
	 ( 'Name', 'Niceman'),      # : 가 아니라 ,를 사용(원래 list가 ,를 사용하기 때문)
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(                      # 이렇게 표현이 가능 -> 아주 좋음!! (구조체 같은 느낌)
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(c), e)
print('f - ', type(c), f)
print()

# 출력
print('a - ', a['name'])        # 존재 X -> error 발생
print('a - ', a.get('name'))    # 존재 X -> None 처리, so get을 사용하는 것이 좀 더 안전하다
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))
print()

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

#삭제
#del a['name']                # key가 name인 key :value 쌍 삭제

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys())         # .key() : key 값들만 뽑아오는 함수
print(">>>>>keys")
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print()

print(">>>>>list of keys")
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

print(">>>>>values")
print('a - ', a.values())           # value들만 뽑아옴
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())
print()

print(">>>>>list of values")
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))
print()

print(">>>>>items")
print('a - ', a.items())            # (key,value)를 tuple형태로
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())
print()

print(">>>>>list of items")
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))
print()

print('a - ', a.pop('name'))
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))
print('d - ', d.pop('City'))

print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
# 예외
# print('f - ', f.popitem())        #empty
print()

print('a - ', 'name' in a)          # 'name'이라는 key가 있나?
print('a - ', 'addr' in a)

# 수정
f.update(Age=36)                # Age라는 key의 value값을 36으로 변경

temp = {'Age': 27}

print('f - ', f)

f.update(temp)

print('f - ', f)

# 선언 : {key : Value}
a = {1 : 'hi'}
b = {'a' : [1,2,3,]}
c = {'name' : 'Zino', 'phone' : '010 1234 5678', 'birth' : '0801'}

print(a)
print(b)
print(c)
