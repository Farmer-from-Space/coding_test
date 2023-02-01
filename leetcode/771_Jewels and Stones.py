class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        ans = 0
        stones = Counter(stones)
        for j in jewels:
            ans += stones[j]
        return ans