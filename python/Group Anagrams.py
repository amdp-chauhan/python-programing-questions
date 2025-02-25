"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(word)) for word in strs]
        # print(strs, sorted_strs)
        anagram_dict = {}
        for i in range(len(sorted_strs)):
            if sorted_strs[i] in list(anagram_dict.keys()): anagram_dict[sorted_strs[i]].append(strs[i])
            else: anagram_dict[sorted_strs[i]] = [strs[i]]

        # print('anagram_dict, ',anagram_dict)
        return list(anagram_dict.values())
