class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for i in s:
            counter[i] -= 1
            if i in seen:
                continue
            
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(i)
            seen.add(i)
        return ''.join(stack)