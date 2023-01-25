# 작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
# 단, 작물의 이름을 직접 입력하여 출력하지 않는다.


grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

# max값을 비교해서 넣고, max에 맞는 이름을 출력한다.
# max = 0
# max_name = ''
# for i in grain_lst:
#     if i[1] > max:
#         max = i[1]
#         max_name = i[0]
    
# print(max_name)



# 메소드를 써보자

grain_lst.sort(key = lambda x : x[1]) # 무엇을 기준으로 sort할건지 정할 수 있다.
# 람다를 활용해서.... 특정 key를 이용해서
# stack overflow 활용해서 찾아보장

print(grain_lst[-1][0])


# 교수님 풀이
dict(grain_lst) # 딕셔너리형태 가능

# 제일 비싼애의 index 번호를 찾는다.
key = list(grain_lst.keys())
value = list(grain_lst.values())

max_value = max(value)
print(max(value.index(max(value))))

max_idx = value.index(max_value)
print(key[max_idx])

