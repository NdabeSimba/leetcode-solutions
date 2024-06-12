# 1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans, maga = dict(), dict()

        for ran in ransomNote:
            if ran in rans:
                rans[ran] += 1
            else:
                rans[ran] = 1

        for mag in magazine:
            if mag in maga:
                maga[mag] += 1
            else:
                maga[mag] = 1

        for key in rans.keys():
            if not key in maga.keys():
                return False
            else:
                if rans[key] <= maga[key]:
                    continue
                else:
                    return False

        return True


# 2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashtable = dict()

        for ch in magazine:
            if ch in hashtable:
                hashtable[ch] += 1
            else:
                hashtable[ch] = 1

        for ch in ransomNote:
            if ch in hashtable:
                if hashtable[ch] > 0:
                    hashtable[ch] -= 1
                else:
                    return False
            else:
                return False

        return True
