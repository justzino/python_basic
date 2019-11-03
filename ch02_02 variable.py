# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))      # type(n) : n의 자료형

# 동시 선언
x = y = z = 700

# 출력
print(x, y ,z)

#선언
var = 75

# 출력
print(var)
print(type(var))

# 재 선언
var = "Change Value"

# 출력
print(var)
print(type(var))


# Object References
# 변수 값 할당 상태일 때 일어나는 일
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

# 예1)
print(300)

# 예2)
# n -> 777
n = 777

print(n)
print(type(n))

m = n
# m-> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400
# m-> 400, 777 <-n

print(m)
print(type(m))


# id(identity)확인 : 객체의 고유값 확인
# 1. 동일한 객체 여부를 판별하는 연산자입니다.
# 2. id() 함수는 객체를 입력값으로 받아서 객체의 고유값(레퍼런스)을 반환하는 함수입니다.
# 3. id는 파이썬이 객체를 구별하기 위해서 부여하는 일련번호입니다. 숫자로서 의미는 없습니다.
# 4. id는 동일한 객체 여부를 판별할 때 사용합니다.

m = 800
n  = 655

print(id(m))
print(id(n))

# 같은 오브젝트 참조
m = 800
n = 800         # 굳이 지금부터 똑같은 값을 할당하는게 비효율적이라고 생각하기 때문에, 내부에서는 아직 하나의 오브젝트로만 존재
                # n의 값이 변경되면 그때부터 할당하여 사용됨
print(id(m))
print(id(n))

# 다양한 변수 선언
# Camel Case :  numberOfCollegeGraduates        -> Method
# Pascal Case :  NumberOfCollegeGraduates       -> Class / 변수에는 X
# Snake Case :  number_of_college_graduates     -> Variable (변수)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능 (python reserved words)
"""
False	def	if	raise
None	del	import	return
True   	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
"""
