class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        output = ''
        path = path.split('/')
        print(path)
        for i in path:
            if i =='..':
                if stack:
                    stack.pop()
            elif i and i!='.':
                stack.append(i)
        if not stack:
            return '/'
        for i in stack:
            output =  output +'/' +i
        return output
                
        
