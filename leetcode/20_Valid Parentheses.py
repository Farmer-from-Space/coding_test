# 맘에 안듬
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in s:
            if i =='(' or i =='[' or i =='{':
                temp.append(i)
            elif i ==')' or i ==']' or i =='}':
                if not temp:
                    return False
                if i ==')' and temp.pop()!= '(':
                    return False
                elif i ==']' and temp.pop()!= '[':
                    return False
                elif i =='}' and temp.pop()!= '{':
                    return False
        if temp:
            return False
        return True