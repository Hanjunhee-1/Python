'''
int() -> 정수로
float() -> 실수로
str() -> 문자열로
bool() -> 불리언으로
None -> 아무것도 없음

실수에 대한 반올림이 필요하다면 int() 함수 말고 round() 함수 사용할 것. int()는 그냥 버림
'''

age = int(input("나이를 입력해주세요: "))
print(type(age))

height = float(input("키를 입력해주세요: "))
print(type(height))

name = str(input("이름을 입력해주세요: "))
print(type(name))

is_student = bool(input("학생인가요? (True/False): "))