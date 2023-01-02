class Solution:
    def generateParenthesis(self, num: int) -> List[str]:

        def generate_rec(open_count, close_count, current_path, result):
            if open_count == num and close_count == num:
                result.append(current_path)
                return

            if open_count < num:
                generate_rec(open_count + 1, close_count, current_path + '(', result)
            if close_count < open_count:
                generate_rec(open_count, close_count + 1, current_path + ')', result)

        result = []
        generate_rec(0, 0, '', result)
        return result
