# 주민등록번호 앞의 6자리는 생년월일이고, 뒤 7자리는 성별, 지역, 오류검출코드이다.
# 주민등록번호를 입력받아 주민등록번호 뒷자리를 비식별화하는 함수 de_identify 를 만들어라.

# 앞 6자리는 그대로 나타내고, 나머지는 *처리하되, 항상 7개로 만들기

# def de_identify(num):
#     number = ''
#     for i in range(0, 6):
#         number += num[i]
    
#     return number + '*******'

# 쉽게하기

def de_identify(num):
    return num[0:6] + '*******'


# 메소드로 넣기해보자

def de_identify(num):
    
    if '-' in num:
        id = num.split('-')
    
        return id[0] + '*******'

    else:
        return num[0:6] + '*******'


# 교수님 풀이
# 함수 변수는 인자를 하나만 받는다.
# 함수 정의시 매개변수는 한 개만 된다.

def de_identify(string):
    # 문자열이 가진 특성상 원본을 바꿀 수 없으니 변경된 값을 변환

    result = string.replace('-', '')
    real_result = ''

    for char in result:
        idx += 1
        if idx >= 6:
            real_result += '*'
        else:
            real_result += char
        idx += 1
    
    result[6:] = ['*']*7 


    






# A. 입력예시
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))


# B. 출력예시
# 970103*******
# 861123******* 
