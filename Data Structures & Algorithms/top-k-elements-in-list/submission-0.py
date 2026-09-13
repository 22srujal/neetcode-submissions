class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        freq= [[] for i in range(len(nums)+1)]

        for j in nums:
            count[j] = 1 + count.get(j, 0)
        
        for i, n in count.items():
            freq[n].append(i)
        
        res= []
        for m in range(len(freq)-1, 0, -1):
            for h in freq[m]:
                res.append(h)

                if len(res) == k:
                    return res





        
             

        