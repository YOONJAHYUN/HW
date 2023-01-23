def group_anagrams(words):
    # 하나의 단어에서 애너그램으로 만들 수 있는 모든 단어를 모은다.
    # 딕셔너리 형태로 만들어서, 값들을 비교해 같은 값을 가진 key값들을 따로 list로 만들어준다.
    
    new_words = {} # 빈 딕셔너리 만들기
    for word in words:
        # dic[key] = value : key 값에 value 넣기
        new_words[word] = [word[0] + word[2] + word[1], word[1] + word[2] + word[0], word[1] + word[0] + word[2], word[2] + word[0] + word[1], word[2] + word[1] + word[0]]
    # print(new_words)

    # value 값들만 모아서 key 값 하나하나와 비교해서 같은 것이 있는지 찾는다.
    # anagram_words = []
    # for new_word_list in new_words.values(): # value 값들만 추출하기
    #         for new_word in new_word_list: # list안의 단어 하나씩 추출하기
    #             for i in new_words.keys():
    #                 if i == new_word:
    #                     if i not in anagram_words:
    #                         anagram_words += [i]
    #                         print(anagram_words)

    # for key in new_words:
    #     for value in new_words[key]:
    #         if key == value:
    #             anagram_words.append(key)


    #             print(anagram_words)

    # value_list = new_words.values()
    # print(value_list)
    anagram_words = []
    for key1 in new_words:
        for key2 in new_words:
            for value2 in new_words[key2]:
                if key1 == value2:
                    anagram_words += [[key1, key2]]
                    
                    print(anagram_words)


            # if new_words == new_word:
            #     print(new_words)

    # for i in new_words.keys():
        

# def group_anagrams(words):
#     new_words = ()
#     anagram_words = []
#     for word in words:
#         new_words[word] = [[word[0] + word[2] + word[1], word[1] + word[2] + word[0], word[1] + word[0] + word[2], word[2] + word[0] + word[1], word[2] + word[1] + word[0]]] 
#     print(new_words)
#     #     for new_word in new_words:
#     #         if word == new_word:
#     #             if word not in anagram_words:
#     #                 anagram_words.append(word)
#     # # anagram_words = []
#     # # for word in words:
#     # #     for new_word in new_words:
#     # #         if word == new_word:
#     # #             if word not in anagram_words:
#     # #                 anagram_words.append(word)
#     # print(anagram_words)

group_anagrams(['eat','tea','tan','ate','nat','bat'])


# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 