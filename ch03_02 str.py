# Chapter03-2
# 파이썬 문자형(str)
# 문자형 중요

#한글 깨짐 방지
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print()

# 문자열 길이 : len
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
print()

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'

# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)
print()

# Raw String : r을 앞에 붙여주면 \를 있는 그대로 출력
raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"


# Raw String 출력
print(raw_s1)
print(raw_s2)


# 멀티라인 출력 : 문자열이 길어서 멀티라인으로 나눈 것을 출력할 경우
# \사용 : 선언을 할때 \를 써서 다음줄까지 계속 이어 나갈수 있음
multi_str1 = \
    """
    문자열
    멀티라인 입력
    테스트
    """

print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(3 * str_o1)           # 곱한만큼 반복
print(str_o1 + str_o2)      # 문자열 합침
#print(dir(str_o1))
print('y' in str_o1)        # str_o1의 문자열 안에 y가 있나?
print('n' in str_o1)
print('P' not in str_o2)    # str_o2의 문자열 안에 p가 있나?
                            #시퀀스 연산자들은 in, not in 사용 가능
print()

# 문자열 형 변환
print(str(66))              # type 확인 : 문자형 66
print(str(10.1))
print(str(True))
print(str(complex(12)))
print()

# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha 등)
# 교재에 나온 함수 (count, find, index, join, upper, lower, lstrip, rstrip, strip, replace, split)
print("Capitalize:\t", str_o1.capitalize())              # .capitalize : 첫글자 대문자
print("endswith?:\t", str_o2.endswith("s"))              # .endswith : 마지막문자가 s로 끝나는가?
print("join str:\t", str_o1.join(["I'm ", "!"]))
print("join str:\t", str_o1.join('ABC'))
print("replace1:\t", str_o1.replace('thon', ' Good'))    # thon -> Good / thon을 찾아서 공백 포함 ' Good'로 대체
print("replace2:\t", str_o3.replace("are", "was"))
print("split:\t\t", str_o4.split(' '))                   # '(단위)' (현재는)공백을 기준으로 문자열을 나눠서 list형태로 반환
print("sorted:\t\t", sorted(str_o1))                     # 문자열을 입력받아 순서를 정렬해서 list형태로 반환
print("reversed1:\t", reversed(str_o2))                  # reverse=True
print("reversed2:\t", list(reversed(str_o2)))            # list 형 변환
print()

# 반복(시퀀스) 설명
im_str = "Good Boy!"

print(dir(im_str))  # ' __iter__'가 있다면 sequence

# 출력
for i in im_str:
    print(i)
print()

# 슬라이싱 : sequence는 슬라이싱 가능
str_sl = 'Nice Python'      # 11 글자

# 슬라이싱 연습
print(str_sl[0:3])              # index 0 1 2(3-1)
print(str_sl[5:])               # [5:11] -> index 5~10
print(str_sl[:len(str_sl)])     # str_sl[0:11] -> index 0~10
print(str_sl[:len(str_sl) - 1])     # str_sl[0:10]
print(str_sl[:])
print(str_sl[1:9:2])            # index 1~8까지 2칸마다 반환
print()
print(str_sl[-5:])              # 뒤에서 5번째 부터 끝까지 [11-5:]
print(str_sl[-4:-2])            # [11-4:11-2] = [7:9]
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])
print()

# 아스키코드
a = 'z'

print(ord(a))
print(chr(122))
