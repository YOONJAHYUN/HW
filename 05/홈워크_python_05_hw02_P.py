 # 1. 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
 # 예를 들어 d(91) = 9 + 1 + 91 = 101일 때,
 # n을 d(n)의 제네레이터(generator)라고 한다. 함수 fn_d(n)을 정의하여 보라


# fn_d(91) 
# 출력 예시 
# 101


# 내 풀이
def fn_d(n):

    result = 0
    for i in str(n):
        result += int(i)
    
    return result + n
    
print(fn_d(91))


# 교수님 풀이) 10으로 나눈 나머지들을 다 계산해서 하나씩 더하기
# 1234를 언제까지? 모든 자릿수를 다 계산할때까지
# 1234 % 10 = 4 :123
# 123 % 10 = 3  :12
# 12 % 10 = 2   :1
# 1 % 10 =1     :0
# 종료 조건이 명확하고, 똑같은 작업을 반복

def fn_d(n):
    # 최종 결괏값
    result = n
    while n != 0:
        result += n % 10 # 4, 3, 2, 1
        n = n // 10
    return result
print(fn_d(91))


# 2. 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1, 3, 5, 7, 9, 20, 31 은 셀프 넘버들이다.
# 셀프넘버를 판별하는 함수 is_selfnumber(n)를 앞서 작성한 fn_d(n) 을 사용하여 작성하라.



def is_selfnumber(n):
    a = n
# 무한반복이 종료하는 시점 1. 셀프넘버일때, 2. 셀프넘버가 아닐때
    while True:

        if fn_d(a) == n: # 무한반복이 멈추는 조건 1
            print('셀프넘버아님')
            break

        if a == 1: # 무한반복이 멈추는 조건 2 a == 1이 되면 셀프넘버가 될 수 밖에 없음
            print('셀프넘버이다')
            break

        a -= 1 # 값이 안나오면 하나씩 줄여서 찾기
        
is_selfnumber()


# 교수님 풀이1) 제너레이터는 나보다 작을 수 없다.

def is_selfnumber(m):
    # m의 제너레이터가 될 수 있는 경우는
    # 1부터 m까지 숫자 중에 있다.
    for i in range(1, m+1):
        # 제너레이터인지 아닌지 판별하는 방법은
        # 숫자 i를 fn_d에 집어 넣었을 때, 그 값이
        # 내가 할당받은 m과 동일하다면
        # i를 m의 제너레이터라고 할 수 있다.


        if fn_d(i) == m: # fn_d(91) == 101 : 91은 101의 제너레이터
            # 하나라도 제너레이터가 없으면?
            # 셀프넘버가 아니므로 셀프 넘버를 판별하는 함수
            # is_selfnumber 함수는 Fasle를 반환하고 종류
            return False

        # else:    
        #     return True
        # 한바퀴만 돌기 때문에 셀프넘버가 아니라도 true 나올 수 있다.
    
    
    # 모든 후보군을 모두 출력했는데 False가 반환되지 않았다면
    # 셀프 넘버가 맞다.
    return True

print(is_selfnumber(101)) # False
print(is_selfnumber(31)) # True


# 교수님 풀이2) lambda함수


def is_selfnumber(m):
    for i in range(1, m+1):
        # lambda [parameter] : expression
        # 모든 자리수의 합 + 본인을 더한 값
        # while 나머지를 사용해서 더해왔는데..
        # 문자열로 바꿔서 각 자리수를 순회하며 더하기도 가능하다.
        # 문자열 1234를 '1' '2' '3' '4'로 변환

        # for char in 'm' : result += char 말고 [int(char) for char in 'm'] => [1, 2, 3, 4] + [m]
        # => sum[1, 2, 3, 4, m]
        fn_d = lambda n: sum([int(char) for char in str(n)] + [n])
        if fn_d(i) == m:
            return False
    return True