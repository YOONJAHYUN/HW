def group_anagrams(words):
    # 하나의 단어에서 애너그램으로 만들 수 있는 모든 단어를 모은다.
    # 딕셔너리 형태로 만들어서, 값들을 비교해 같은 값을 가진 key값들을 따로 list로 만들어준다.

    new_words = {} # 빈 딕셔너리 만들기
    
    for word in words:
        # dic[key] = value : key 값에 value 넣기
        # 정렬된 형태로 넣어서 같은 값이 있는지 비교한다.
        new_words[word] = sorted([word, word[0] + word[2] + word[1], word[1] + word[2] + word[0], word[1] + word[0] + word[2], word[2] + word[0] + word[1], word[2] + word[1] + word[0]])

    print(new_words)

    # value 값들이 같은 것들의 key끼리 묶는다.
    # value를 순차적으로 돌려서 같은 걸 찾는다.
    # anagram = []
    # for 





group_anagrams(['eat','tea','tan','ate','nat','bat'])
