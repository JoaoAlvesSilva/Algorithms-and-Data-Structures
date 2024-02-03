// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_list=[]
        for token in tokens:
            if token == '+':
                val = new_list[-1] + new_list[-2]
                new_list.pop()
                new_list.pop()
                new_list.append(val)
            elif token == '-':
                val = new_list[-2] - new_list[-1]
                new_list.pop()
                new_list.pop()
                new_list.append(val)
            elif token == '/':
                val = int(new_list[-2]/new_list[-1])
                new_list.pop()
                new_list.pop()
                new_list.append(val)
            elif token == '*':
                val = new_list[-2] * new_list[-1]
                new_list.pop()
                new_list.pop()
                new_list.append(val)
            else:
                new_list.append(int(token))
        return new_list[-1]

        