class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        list1 = []
        i = 0
        while i <len(s):
            j = i
            while s[j]!="#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            list1.append(s[i:i+length])
            i += length

        return list1
