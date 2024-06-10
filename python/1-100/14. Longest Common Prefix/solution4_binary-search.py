# binary search
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return
        else:
            target = strs[0]

            remains = strs[1:]
            if not remains:  # strs에 1개 원소밖에 없을 때
                return target
            left = 0
            right = len(target) - 1

            mid = (left + right) // 2
            while left <= right:
                # 공통 글자들인지 확인
                if self.isCommonPrefix(target[: mid + 1], remains):
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2
        return target[: mid + 1]

    def isCommonPrefix(self, target, remains):
        for x in remains:
            if not x.startswith(target):  # 남은 원소들의 시작하는 글자 확인
                return False
        return True


# strs 원소 개수: n
# 각 원소 글자 수: m
# time complexity: O(n×m×logm) -> binary search 시간 복잡도 O(log m),
# 최악의 경우 strs 원소 개수 x 각 원소 글자 수만큼 모두 훑어봐야 함
