class Solution:
    def decodeString(self, s: str) -> str:
        output = ''
        num_stack = []
        string_stack = []
        num_temp = ''
        for i in range(len(s)):
            if s[i] =='[':
                num_stack.append(int(num_temp))
                num_temp = ''
                string_stack.append(output)
                output = ''
            elif s[i] ==']':
                output =  string_stack.pop() + output * (num_stack.pop())

            elif s[i].isdigit():
                num_temp = num_temp + s[i]
            else:
                output = output + s[i]
            
        return output
        
