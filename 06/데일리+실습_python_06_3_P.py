# 1. 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는
# count_vowels 함수를 작성하시오.

def count_vowels(word):
    count = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vowel_list:
            count += 1
    return count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3