class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = ''
        for c in paragraph:
            if not c.isalnum():
                c = ' '
            para += c.lower()
        new_para = para.split()
        word_count = {}
        banned_words = set(banned)
        for word in new_para:
            if word not in banned_words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        return max(word_count.items(),key = lambda x: x[1])[0]
    
        
