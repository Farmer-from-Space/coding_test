from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned) :
        for i in paragraph:
            if not i.isalnum() :
                paragraph = paragraph.replace(i, ' ')
        P = Counter(paragraph.lower().split())
        
        for i,v in sorted(P.items(), key=lambda x: x[1], reverse=True):
            if i not in banned:
                return(i)