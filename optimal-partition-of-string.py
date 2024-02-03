// https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        characters = list(s)
        substrings_list=[]
        word_list=[]
        for character in characters:
            if character not in word_list:
                word_list.append(character)
            else:
                substrings_list.append(word_list)
                word_list=[character]
        return len(substrings_list)+1
