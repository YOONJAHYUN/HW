# 2월이 29일까지 있는 해를 윤년이라고 한다.
# 어떤 해가 입력되면 그 해가 윤년인지 아닌지 판별하시오.

# 윤년판단조건
# 1. 해(year)가 4의 배수이면서 100의 배수가 아니면 윤년.
# 2. 400의 배수이면 윤년
# 3. 위 두조건 중 하나라도 맞으면 윤년이다.

year = int(input())

if ((year % 4 == 0 and year % 100 != 100) or (year % 400 == 0)):
    print('윤년')
else:
    print('윤년아님')