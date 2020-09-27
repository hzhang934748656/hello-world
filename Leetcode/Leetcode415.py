class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        temp = 0
        carry = 0
        res = []
        while p1 >= 0 and p2 >= 0:
            temp1 = ord(num1[p1]) - ord('0')
            temp2 = ord(num2[p2]) - ord('0')
            res.append((temp1 + temp2 + carry) % 10)
            carry = (temp1 + temp2 + carry) // 10
            p1 -= 1
            p2 -= 1
        while p1 >=0:
            temp1 = ord(num1[p1]) - ord('0')
            res.append((temp1 + carry) % 10)
            carry = (temp1 + carry) // 10
            p1 -= 1
        while p2 >=0:
            temp2 = ord(num2[p2]) - ord('0')
            res.append((temp2 + carry) % 10)
            carry = (temp2 + carry) // 10
            p2 -= 1
        if carry:
            res.append(carry)
        return "".join(str(x) for x in res[::-1])            
        
