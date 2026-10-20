from collections import deque

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        d = {str(n): n for n in range(10)}
        temp_prods = [0] * len(num2)
        # calculate temp_prods
        for i in range(len(num2) - 1, -1, -1):
            digit2 = num2[i]
            temp_prods[i] = deque()
            for j in range(len(num2) - i - 1):
                temp_prods[i].appendleft("0")
            carry = 0
            for digit1 in num1[::-1]:
                temp = d[digit1] * d[digit2] + carry
                carry = temp // 10
                res = temp % 10
                # if carry > 9: print("Error")
                temp_prods[i].appendleft(str(res))
            if carry > 0: temp_prods[i].appendleft(str(carry))
            # temp_prods[i] = "".join(temp_prods[i])
            # print(temp_prods[i])

        # sum temp_prods
        # print(temp_prods)
        return self._my_sum(temp_prods)

    def _my_sum(self, temp_prods):
        result = deque()
        for temp_prod in temp_prods:
            # print(result)
            # result = result + temp_prod
            result = self._my_add(result, temp_prod)
            # for i in range(len(temp_prod) - 1, -2, -1):
            #     if i == -1 and carry == 0:
            #         break
            #     temp = result[i] + temp_prod[i] + carry
            #     carry = temp // 10
            #     res = temp % 10
            #     result[i] = str(res)

        return "".join(result)

    def _my_add(self, num1, num2):
        if len(num1) > len(num2):
            for i in range(len(num1) - len(num2)):
                num2.appendleft("0")
        else:
            for i in range(len(num2) - len(num1)):
                num1.appendleft("0")
        result = deque()
        carry = 0
        for i in range(len(num2) - 1, -1, -1):
            temp = int(num1.pop()) + int(num2.pop()) + carry
            carry = temp // 10
            res = temp % 10
            result.appendleft(str(res))
        if carry > 0: result.appendleft(str(carry))
        
        return result