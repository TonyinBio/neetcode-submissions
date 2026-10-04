class Solution:

    def encode(self, strs: List[str]) -> str:
        payload = "😊".join(strs)
        meta = f"{len(strs):03}"
        # print(meta + payload)
        return meta + payload
    def decode(self, s: str) -> List[str]:
        # print(s)
        meta = s[:3]
        if int(meta) == 0: return []
        payload = s[3:]
        return payload.split("😊")