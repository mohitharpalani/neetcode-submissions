from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #bruteforce
        #optimized
        # dict1={}
        # dict2={}
        # for i in s:
        #     if i in dict1:
        #         dict1[i]+=1
        #     else:
        #         dict1[i]=1            

        # for i in t:
        #     if i in dict2:
        #         dict2[i]+=1
        #     else:
        #         dict2[i]=1 
        # return dict1==dict2
        if len(s)!=len(t):
            return False
        for ch in s:
            count1=0
            count2=0
            for c in s:
                if c==ch:
                    count1+=1
            for d in t:
                if d==ch:
                    count2+=1
            if count1!=count2:
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans=[]
        # n=len(strs)
        # visited=[False]*n
        # for i in range(n):
        #     if visited[i]:
        #         continue
        #     subgrp=[strs[i]]
        #     visited[i]=True
        #     for j in range(i+1,n):
        #         if self.isAnagram(strs[i],strs[j]):
        #             visited[j]=True
        #             subgrp.append(strs[j])
        #     ans.append(subgrp)
        # return ans
        # d=defaultdict(list)
        # answer=[]
        # for word in strs:
        #     sortedword = ''.join(sorted(word))
        #     d[sortedword].append(word)
        # for group in groups.values():
        #     answer.append(group)
        # return answer
        groups:defaultdict = defaultdict(list)
        answer=[]
        for word in strs:
            sortedword = ''.join(sorted(word))
            groups[sortedword].append(word)
        for group in groups.values():
            answer.append(group)
        return answer

