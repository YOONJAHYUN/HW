def group_anagrams(words):
    # 하나의 단어에서 애너그램으로 만들 수 있는 모든 단어를 모은다.
    # 딕셔너리 형태로 만들어서, value 값들 정렬해 서로 비교한다.
    # value 값들을 정렬해서 같은 value를 찾는다.
    # 같은 value끼리 anagram이 된다.

    new_words = {} # 빈 딕셔너리 만들기
    
    for word in words:
        # dic[key] = value : key 값에 value 넣기
        # 정렬된 형태로 넣어서 같은 값이 있는지 비교한다.
       
        new_words[word] = sorted([word, word[0] + word[2] + word[1], word[1] + word[2] + word[0], word[1] + word[0] + word[2], word[2] + word[0] + word[1], word[2] + word[1] + word[0]])
        
     
    # 큰 list 하나와 버릴 list 하나를 만들어서 버릴 list를 모아 큰 list에 집어넣는다.
    anagram = []

    for i in new_words: # key값 순회
        arr = []
        for j in new_words: # key값과 key값들 순회
            if new_words[i] == new_words[j]: # key값의 value들이 같으면
                arr.append(j) # arr에 key 추가
            else:
                continue # 같지 않으면 반복

        if arr not in anagram: # arr 중복값 없애기 위해 큰 list에 추가
            anagram.append(arr)

    print(anagram)
        
    # 처음 아이디어는 key값을 value들 중에 있는지 없는지로 할려고 했는데, 하다보니까 그냥 value들끼리 비교하게 됐다.
    # sorted를 써서 비교할거라면 애초부터 group_anagrams값을 sorted했으면 더 편했을 것 같다!



group_anagrams(['eat','tea','tan','ate','nat','bat'])
