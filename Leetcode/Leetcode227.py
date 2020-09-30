class Solution:
    def calculate(self, s: str) -> int:
        n_stack = []
        prev_sign = "+"
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (s[i] != ' ' and s[i] in "+-/*") or i == len(s) - 1:
                if prev_sign == '*':
                    n_stack.append(n_stack.pop()*num)
                elif prev_sign == '/':
                    temp = n_stack.pop()
                    if temp < 0:
                        n_stack.append(-(abs(temp)//num))
                    else:
                        n_stack.append(temp//num)
                elif prev_sign == '+':
                    n_stack.append(num)
                elif prev_sign == '-':
                    n_stack.append(-num)
                num = 0
                prev_sign = s[i]
        return sum(n_stack)
