class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos_word1 = [idx for idx, word in enumerate(words) if word == word1]
        pos_word2 = [idx for idx, word in enumerate(words) if word == word2]
        loc = []
        for i in range(len(pos_word1)):
            for j in range(len(pos_word2)):
                loc.append(abs(pos_word1[i] - pos_word2[j]))
                
        return min(loc)
