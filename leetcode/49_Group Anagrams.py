class Solution:
    def groupAnagrams(self, strs) :
        ans = [] 
        dic =  dict()
        for i in range(len(strs)):     
            p = ''.join(sorted(list(strs[i])))
            if p in dic:
                ans[dic[p]].append(strs[i])
            else:
                dic[p] = len(ans)
                ans.append([strs[i]])           
        
        return ans