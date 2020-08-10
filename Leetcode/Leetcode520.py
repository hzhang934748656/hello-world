class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return word.islower() or word.isupper()
        if word[0].islower():
            for letter in word[1:]:
                if letter.isupper():
                    return False
            return True
        elif word[0].isupper() and word[1].islower():
            for letter in word[1:]:
                if letter.isupper():
                    return False
            return True
        elif word[0].isupper() and word[1].isupper():
            for letter in word[1:]:
                if letter.islower():
                    return False
            return True
            
        
        
