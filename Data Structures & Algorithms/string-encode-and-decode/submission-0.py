class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s + "é"
        print("encode result: ",result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        word = ""
        for i in s:
            if (i == "é"):
                result.append(word)
                word = ""
            else:
                word = word + i
        print("decode result: ", result)
        return result
