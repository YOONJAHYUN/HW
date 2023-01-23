# 김코딩은 타임머신을 개발했다. 적절한 날짜를 정하기 위해서 날짜를 분석하는 프로그램이 필요하다. 다음 조건을 만족하는 프로그램을 완성하라.

# 연도, 월, 일을 순서대로 입력받는다.
# 윤년으로 가면 타임머신에 에러가 생긴다. 윤년을 입력했을 경우 연도를 다시 입력받아야 한다.
# 윤년이 아닌 연도를 입력받을 경우, 날짜를 편하게 정할 수 있도록 해당 연도의 달력을 출력하라.
# 김코딩은 월요일을 싫어한다. 입력한 날짜가 월요일인 경우 경고 메시지를 출력하라.
# 입력이 완료되면 연, 월, 날짜, 그리고 요일을 dictionary에 정리하여 출력하라.
# HINT: calendar 모듈을 활용하라.	(공식문서 링크)

# calendar 모듈사용
import calendar
# 제일 먼저 year값을 받는다.
year = int(input())

# 윤년이 아닐 때까지 순환한다.
while True:
    if calendar.isleap(year) == True:
        year = int(input('윤년입니다. 연도를 다시 입력해주세요.'))

    else:
        print(calendar.calendar(year))
        break # 순환 탈출 조건

# 순환이후, 달과 일자를 받는다.
month = int(input())
date = int(input())

# 요일을 계산해주는 함수 지정
day = calendar.weekday(year, month, date)
# 월요일 경고창, 월요일은 0이다.
if calendar.weekday(year, month, date) == 0:
    print(f'경고 월요일입니다.')

# 숫자마다 나타내는 요일이 다르므로 딕셔너리 형태로 넣어주고, value 값을 반환한다.
day_kor = {0 : '월요일', 1 : '화요일', 2 : '수요일', 3 : '목요일', 4 : '금요일', 5 : '토요일', 6 : '일요일', }

your_day = {'년': year, '월': month, '일': date, '요일': day_kor[day]}

print(your_day)










# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}


