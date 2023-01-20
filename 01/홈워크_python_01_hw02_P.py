s = input('숫자를 입력해주세요 : ')
# print(s) # 문자열 1234 -> 각 자릿수를 더하라 -> 1 + 2 + 3 + 4

# 리스트로 바꾸기
# arr = list(s)
# print(arr)
# result = 0
# for char in arr: # char -> '1' '2' '3' '4'
#     result = result + int(char)
# 어떤 값을 연산한 후에 다시 본인에게 할당을 할때는
# 할당 연산자를 사용하면 편하다.
# result = int(char)

# print(result)


# 문자열을 순회
result = 0

for char in s: # '1' '2' '3' '4'
    result = result + int(char)
print(result)



# 문자열 1234를 숫자 1234로 바꾼 다음 10씩 나눈 나머지를 더해 나간다.



# map(function, iterable) -> 순회 가능한 요소가 가진 각 값들을 첫번째로 작성한 함수에 각각 넣어서 실행
print(sum(map(int, s)))

# 문자열 = immutable : 변경불가능
# str이 가지고 있는 함수 중에, join 함수
# 'some str'.join(iterable)
print('+'.join(s)) # s = '1234' -> '1+2+3+4'
print(eval('1+2+3+4'))