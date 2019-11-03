# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)       # 시퀀스 : 줄, 순서
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
'''

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
float_v = 10.0          # 밑에서 float사용해야해서 변경
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (3, 5, 7)       # tuple = 3, 5, 7 이렇게 해줘도 tuple
set = {7, 8, 9}

# 주의 : [],(),{} 는 각각 list, tuple, set 자료형 선언시 사용되므로 다름을 인지

print(dict)

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(bool))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

print()

# 숫자형 연산자
"""
+   -   *   /
// : 몫
% : 나머지
abs(x) : 절댓값
int(x)
float(x)
complex(x)
pow(x, y) == x ** y      # x의 y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 999999999999999999999999999999999999999      #알아서 필요한만큼 메모리 할당

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

print()

# 연산 실습
i1 = 39
i2 = 15
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# -
print(">>>>> -")
print("i1 - i2: ", i1 - i2)
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)

# *
print(">>>>> *")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)

# /
print(">>>>> /")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)
print()

# // 몫
print(">>>>> //")
print("i2 // i1: ", i2 // i1)
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)

# % 나머지
print(">>>>> %")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)

# ** 제곱
print(">>>>> **")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2)
print("f1 ** f2: ", f1 ** f2)

print()

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))
print()

# 형 변환
print(float(b))  # 정수 -> 실수
print(int(c))  # 실수 -> 정수
print(int(d))  # 실수 -> 정수
print(int(True))  # Bool -> 정수
print(float(True))  # Bool -> 정수
print(int(False))  # Bool -> 정수
print(float(False))  # Bool -> 정수
print(complex(3))  # 정수 -> 복소수
print(complex('3'))  # 문자 -> 복소수
print(complex(False))  # Bool -> 복소수
print()

# 수치 연산 함수
print(abs(-7))              # 절댓값
x, y = divmod(100, 8)       # 몫과 나머지를 변수 두개로 한번에 할당
print(x, y)
print(pow(5, 3), 5 ** 3)    # 5의 3제곱

#외부 모듈
import math                 #

#ceil
print(math.ceil(5.1))       # 5.1이상의 수 중에서 가장 작은 정수

#floor

#pi
print(math.pi)
