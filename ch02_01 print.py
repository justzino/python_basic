# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# 기본 출력
print('Python Start!')
print("Python Start!")
print("""Python Start!""")
print('''Python Start!''')

print()

# separator 옵션 사용
print('P', 'Y', 'T', 'H','O','N', sep='')       # default = ' '
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')    #print문은 자동 개행이 되지만, end= 이 뒤에 오면 이걸로 개행을 대체
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션 사용
import sys

print('Learn Python', file=sys.stdout)  #'Learn Python'을 내가 지정한 외부파일 sys.stdout에 쓸거다

print()

# format 사용(d, s, f) (d: digit, s: string, f: float)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))   #index
print('{0} {1}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice',))           # %10s : 총 10개의 자리를 확보, 오른쪽 정렬
print('{:>10}'.format('nice'))      # {:>10} : 총 10개의 자리를 확보, 오른쪽 정렬

print('%-10s' % ('nice'))           # %-10s : 총 10개의 자리를 확보, 왼쪽정렬
print('{:<10}'.format('nice'))      # {:<10} : 총 10개의 자리를 확보, 왼쪽정렬
print('{:10}'.format('nice'))       # {:10} : 총 10개의 자리를 확보, 왼쪽정렬

print('{:_<10}'.format('nice'))     # {:_<10} : 빈칸을 _로 채움
print('{:^10}'.format('nice'))      # {:^10} : 중앙정렬

print('%.5s' % ('pythonstudy'))             # %.5s : 5칸 이상부터 절삭
print('{:.5}'.format('pythonstudy'))        # {:.5} : 5칸 이상부터 절삭
print('{:10.5}'.format('pythonstudy'))      # {:10.5} : 총 10개의 자리를 확보, 5개만 출력

print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))       # 정수일때는 {}안에 자리수 확보할때 d사용해야함 (s는 안했음)

print()

# %f
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))
print('%1.7f' % (3.141592653589793,))       # %1.7f : 정수부 1자리, 소수부 7자리 출력

print('%06.2f' % (3.141592653589793,))      # %06.2f : 총 6자리, 소수부 2자리 출력 -> 003.14
print('%06.2f' % (35354231.234,))
print('{:06.2f}'.format(3.141592653589793))
