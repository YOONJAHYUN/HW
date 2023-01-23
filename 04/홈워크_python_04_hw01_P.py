# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 	조건
# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.




words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]



# length = 0
# for i in words:
#     print(words[length][-1] == words[length+1][0])
#     length += 1




# 앞에랑 뒤랑 같은지 확인하기위해 담아야됨
dupliccated_word = []

# 처음부터 words의 길이보다 1 작은 위치를 조회 할 때 까지 반복
idx = 0

while idx < len(words) - 1:
    if words[idx][-1] == words[idx + 1][0] and words[idx] not in dupliccated_word:
        dupliccated_word += [words[idx]] # 리스트로 만들면 단어단위로 들어간다

    else:
        print(f'{idx+1}번째가 탈락했습니다.')   
        break
    idx += 1
print(dupliccated_word)

# try except 쓴 버전
for i in range(len(words)):
    try:
        if ((words[i][-1] == words[i+1][0]) and (words[i] not in new)):
            new.append(words[i])
        else:
            print(f'{i+1}번째 사람이 틀렸습니다.')

    except:
        break

    