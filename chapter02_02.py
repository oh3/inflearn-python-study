# Chapter02-1
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(n * 700)

#클래스의 타입을 보여줌
print(type(n))

# 동시 선언
x = y = z = 700
print(x,y,z)

# 선언
var = 75

# 재선언

var = "Change Value"
print(var)
print(type(var))

# Object Reference
# 변수의 값이 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))

m = n
# m -> 777 <- # NOTE:

print(m, n)
print(type(m), type(n))

m = 400
print(m)

# id(identiy) 확인 : 객체의 고유값 확인

m = 800
n = 655

# 오브젝트의 고유값
print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 같은 오브젝트 참조
# 파이썬을 효율성을 위해 내부적으로 똑같은 변수를 하나의 오브젝트로 표시함
m = 800
n = 800
z = 800
i = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#그래서 결과 는 true

# 다양한 변수선언
# camel Case : numberOfColleageGraduates -> Method
# Pascal Case : NumberOfColleageGraduates -> class
# Sanke case : number_of_colleage_graduates -> 변수

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
# for, as, class 등등
