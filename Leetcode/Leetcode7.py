class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x)
        while a!=0:
            temp = a % 10
            a = int(a / 10)
            num = num * 10 + temp
        
        #  123
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <=2147483648:
            return -num
        else:
            return 0
