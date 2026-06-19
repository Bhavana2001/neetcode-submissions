class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s + "é"
        return result

    def decode(self, s: str) -> List[str]:
        result = s.split("é")
        result = result[:-1]
        
        return result
        
