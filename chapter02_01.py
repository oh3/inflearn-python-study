# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

#프린트에 공백 넣으면 개행됨
print()

# Separator 옵션               sep=' '  분리가 무엇으로 되어있냐
# 원하는 포맷 형식으로 출력할 때 사용함
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')

#웹에서 전화번호를 가져왔을 때 변환
print('010', '7777', '1234', sep='-')

#메일주소로 변환
print('python', 'google.com', sep='@')

print()

#end 옵션
#end 옵션이 들어간 문자로 다음 print 문에 이어질 수 있게됨
print('Welcome to', end=' ')
print('It News', end=' ')
print('Web site')

print()

#file 옵션
import sys

#현재 이 내용을 내가 외부에 하드디스크에 특정 파일로 쓸 것이다.
#sys.stdout -> 콘솔에 쓸거다.
print('Learn Python', file=sys.stdout)
print()

#format 사용(d : 정수 3, s : 문자 'python' , f : 실수 3.141591 )
print('%s %s' % ('one','two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))#공백을 _로 채움
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('python study')) # 원하는 자릿수 만큼 절삭

print('{:10.5}'.format('pythonstudy')) # 10자릿수 확보하고 5개만 나와라

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print ('{:4d}'.format(42))

print()

# %f
#   정수부 소수부 지정 가능
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))

test
