class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def combinations(open_para, close_para, para):
            ans = []
            if open_para == close_para == n:
                return [para]
            elif open_para > n:
                return []

            if open_para > close_para:
                ans += combinations(open_para, close_para + 1, para + ")")
            
            ans += combinations(open_para + 1, close_para, para + "(")

            return ans

        return combinations(0, 0, "")