class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        splitwords = words[:k]
        "".join(str(splitwords))
        return splitwords
        
        
        
s = str(input("phrase: "))
k = int(input("number: "))

print("splitwords")