class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = list(map(int, str(int(a) + int(b))))

        for i in range(len(temp) - 1, 0, -1):
            if temp[i] == 2:
                temp[i] = 0
                temp[i - 1] += 1

            if temp[i] > 1:
                if temp[i] == 2:
                    temp[i] = 0
                    temp[i - 1] += 1
                else:
                    temp[i] = temp[i] // 2
                    temp[i - 1] += temp[i] % 2

        if temp[0] > 1:
            if temp[0] == 2:
                temp[0] = 0
                temp.insert(0, 1)
            else:
                tnum = temp[0]
                temp[0] = tnum // 2
                temp.insert(0, tnum % 2)

        result = str()

        for num in temp:
            result += str(num)

        return result


self = Solution()

a = "11"
b = "1"
print(Solution.addBinary(self, a, b))

a = "1010"
b = "1011"
print(Solution.addBinary(self, a, b))
