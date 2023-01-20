score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90 # 항목추가

# score['python'] = 85 # 값 재할당

score.update({'python':85}) 
# 한번에 여러개의 함수를 바꿀 수 있다.
# score.update({'python':85, 'django':60})


# 1. score가 가진 모든 값을 순회
# 2. score.update({'python' : 85, 'django': 60})
# 3. score의 전체 길이를 구해 나간다.
    # 3-1. 순회시 마다 1씩 커지는 변수

total = 0
lenth = 0
# dict 순회시에는 key를 순회한다.
for key in score:
    # print(score[key]) # score['python']
    total = total + score[key]
    # total += score[key]
    lenth = lenth + 1
# 모든 순회가 다 끝나고 난 뒤
print(total/lenth)


print(sum(score.values())/len(score.values()))