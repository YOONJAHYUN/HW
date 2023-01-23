def group_anagrams(words):
    # 하나의 단어에서 애너그램으로 만들 수 있는 모든 단어를 모은다.
    # 딕셔너리 형태로 만들어서, 값들을 비교해 같은 값을 가진 key값들을 따로 list로 만들어준다.
    
    alphabet = {}

    for word in words:
        
        for i in word:

            alphabet[i] = word.count(i)

            print(alphabet)

group_anagrams(['eat','tea','tan','ate','nat','bat'])


# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 