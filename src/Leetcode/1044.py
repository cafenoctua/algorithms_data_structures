class Solution:
    def defangIPaddr(self, address: str) -> str:
        # address_proc = ""
        # for i in range(len(address)):
        #     if address[i] == ".":
        #         address_proc += "[" + address[i] + "]"
        #     else:
        #         address_proc += address[i]    
        # return address_proc

        a = ["["+i+"]" if i == "." else i for i in address]
        b = ""
        for i in a:
            b += i
        return b

solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))