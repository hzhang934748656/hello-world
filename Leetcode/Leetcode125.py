class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    temp.append(i.lower())
                else:
                    temp.append(i)
        print(temp)
        return temp == temp[::-1]
        
