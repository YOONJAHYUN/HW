def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError: # 안적으면 모든 예외상황이 except로 넘어간다 그래서 정확하게 zerodivisionerror라고 말해주는 것.
        return '0으로 나눌 수 없습니다.'
    except TypeError:
        print ('정수 이외의 값으로 나눌 수 없습니다.')