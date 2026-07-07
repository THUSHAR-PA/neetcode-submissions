class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i!='+' and i != '-' and i != '*' and i != '/':
                stack.append(i)
            if i == '+':
                val1=stack.pop()
                val2=stack.pop()
                val3 = int(val2) + int(val1)
                stack.append(val3)
            if i == '-':
                val1=stack.pop()
                val2=stack.pop()
                
                val3 = int(val2) - int(val1)
                stack.append(val3)
            if i == '*':
                val1=stack.pop()
                val2=stack.pop()
                val3 = int(val2) * int(val1)
                stack.append(val3)
            if i == '/':
                val1=stack.pop()
                val2=stack.pop()
            
                if val1 == 0:
                    val3 = 0
                else:
                    val3 = int(val2)/int(val1)
                stack.append(val3)
        return int(stack[0])
        